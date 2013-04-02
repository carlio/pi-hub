from celery.schedules import crontab
from celery.task import task, periodic_task
import requests
from pypackages.models import PackageRelease, PythonPackage, FetchStatus
import logging
from django.utils import timezone
from pyquery import PyQuery as pq
import pytz
from django.conf import settings
import xmlrpclib


def _get_client():
    return xmlrpclib.ServerProxy('http://pypi.python.org/pypi', use_datetime=True)

def _open(url):
    headers = { 'User-Agent': settings.SCRAPER_USER_AGENT }
    resp = requests.get(url, headers=headers)
    return resp.content

#
#@periodic_task(run_every=crontab(minute=0, hour=0))
#def check_fetch_index():
#    state = get_mirror_state()
#    state.index_fetch_status = FetchStatus.FETCHING
#    state.save()
#    fetch_index.delay()


@task
def fetch_index():
    index = pq(url='http://pypi.python.org/simple/', opener=_open)
    for anchor in index.find('a'):
        package_name = pq(anchor).text()
        PythonPackage.objects.get_or_create(name=package_name)


@task
def fetch_releases():
    for pkg in PythonPackage.objects.filter(fetch_status=FetchStatus.NOT_STARTED):
        pkg.fetch_status = FetchStatus.FETCHING
        pkg.save()
        fetch_releases_for_package.delay(pkg)


@task
def fetch_releases_for_package(python_package, async=True):

    releases = python_package.sync()

    for release, is_new in releases:
        if is_new:
            fetch_release_info.delay(release)

    python_package.fetch_status=FetchStatus.COMPLETE
    python_package.last_sync = timezone.now()
    python_package.save()


@task
def fetch_release_info(release):

    logging.debug('fetching %s'% release)
    package_name = release.python_package.name
    version = release.version 
    
    client = _get_client()
    data = client.release_data(package_name, version)
    release_data = ReleaseData(release=release)
    for key, value in data.iteritems():
        if value == 'UNKNOWN':
            continue
        if hasattr(release_data, key):
            setattr(release_data, key, value)
    
    if not ReleaseData.objects.filter(field_hash=release_data.calculate_hash()).exists():
        release_data.save()
    
    urls = client.release_urls(package_name, version)
    release_url = ReleaseUrl(release=release)
    for url in urls:
        print url
        for key, value in url.iteritems():
            if value == 'UNKNOWN':
                continue
            
            if key == 'upload_time':
                release_url.upload_time = value.replace(tzinfo=pytz.UTC)
            
            elif hasattr(release_url, key):
                setattr(release_url, key, value)
                
        if not ReleaseUrl.objects.filter(field_hash=release_url.calculate_hash()).exists():
            release_url.save()
    