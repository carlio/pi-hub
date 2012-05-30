from celery.task import task
import xmlrpclib
from pihub.packages.models import Release, Pkg, ReleaseData, ReleaseUrl
import logging
import pytz


def _get_client():
    return xmlrpclib.ServerProxy('http://pypi.python.org/pypi', use_datetime=True)


@task
def fetch_index():
    packages = _get_client().list_packages()
    for package_name in packages:
        pkg, _ = Pkg.objects.get_or_create(name=package_name)
        fetch_releases.delay(pkg)
        

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
        if hasattr(release_data, key):
            setattr(release_data, key, value)
    release_data.save()
    
    urls = client.release_urls(package_name, version)
    release_url = ReleaseUrl(release=release)
    for url in urls:
        for key, value in url.iteritems():
            if key == 'upload_time':
                value
                release_url.upload_time = value.replace(tzinfo=pytz.UTC)
            
            elif hasattr(release_url, key):
                setattr(release_url, key, value)
    release_url.save()
    