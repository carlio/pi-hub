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
    # clean out the old packages so we don't need to do
    # expensive get_or_create calls each time
    # but make sure we leave private packages intact
    Pkg.objects.filter(private=False).delete()
    
    packages = _get_client().list_packages()
    pkg_list = []
    for package_name in packages:
        # TODO: this needs to be broken up when using sqlite - see
        # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create
        pkg_list.append(Pkg(name=package_name))
    Pkg.objects.bulk_create(pkg_list)
        
    state = get_mirror_state()
    state.index_fetch_status = FetchStatus.COMPLETE
    state.save()
 
    fetch_releases.delay()
        

@task
def fetch_releases():
    pkgs = Pkg.objects.filter(fetch_status=FetchStatus.NOT_STARTED)
    pkg_count = pkgs.count()
    for i in range(0, pkg_count, 100):
        fetch_releases_for_packages.delay( pkgs[i:i+100] )


@task
def fetch_releases_for_packages(pkgs, async=True):  
    
    pkgs.update(fetch_status=FetchStatus.FETCHING)
    call = xmlrpclib.MultiCall(_get_client())
    
    for pkg in pkgs:
        call.package_releases(pkg.name, True)

    try:
        pkgs_versions = zip(pkgs, call())
    except xmlrpclib.Fault, err:
        logging.error("XMLRPC Fault: code=%s, message=%s" % (err.faultCode, err.faultString))
        pkgs.update(fetch_status=FetchStatus.NOT_STARTED)
        return
      
    for pkg, versions in pkgs_versions:
        for version in versions:
            release, _ = Release.objects.get_or_create(version=version, pkg=pkg)
            if async:
                fetch_release_info.delay(release)
            else:
                fetch_release_info(release)
                
    pkgs.update(fetch_status=FetchStatus.COMPLETE)
            

@task
def fetch_release_info(release):
    print 'fetching %s'% release
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
    