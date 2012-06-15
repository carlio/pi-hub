from celery.schedules import crontab
from celery.task import task, periodic_task
from pihub.packages.models import Release, Pkg, ReleaseData, ReleaseUrl, \
    get_mirror_state, FetchStatus
import logging
import pytz
import xmlrpclib


def _get_client():
    return xmlrpclib.ServerProxy('http://pypi.python.org/pypi', use_datetime=True)


@periodic_task(run_every=crontab(minute=0, hour=0))
def check_fetch_index():
    state = get_mirror_state()
    state.index_fetch_status = FetchStatus.FETCHING
    state.save()
    fetch_index.delay()


@task
def fetch_index():
    packages = _get_client().list_packages()
    for package_name in packages:
        pkg, _ = Pkg.objects.get_or_create(name=package_name)
        #fetch_releases.delay(pkg)
        
    state = get_mirror_state()
    state.index_fetch_status = FetchStatus.COMPLETE
    state.save()
        

@task
def fetch_releases(pkg):
    try:
        versions = _get_client().package_releases(pkg.name, True)
    except xmlrpclib.Fault, err:
        logging.error("XMLRPC Fault: code=%s, message=%s" % (err.faultCode, err.faultString))
    else:
        for version in versions:
            release, _ = Release.objects.get_or_create(version=version, pkg=pkg)
            fetch_release_info.delay(release)



@task
def fetch_release_info(release):
    package_name = release.pkg.name
    version = release.version 
    
    client = _get_client()
    data = client.release_data(package_name, version)
    release_data = ReleaseData(release=release)
    for key, value in data.iteritems():
        if value == 'UNKNOWN':
            continue
        if hasattr(release_data, key):
            setattr(release_data, key, value)
    release_data.save()
    
    urls = client.release_urls(package_name, version)
    release_url = ReleaseUrl(release=release)
    for url in urls:
        for key, value in url.iteritems():
            if value == 'UNKNOWN':
                continue
            
            if key == 'upload_time':
                release_url.upload_time = value.replace(tzinfo=pytz.UTC)
            
            elif hasattr(release_url, key):
                setattr(release_url, key, value)
        release_url.save()
    