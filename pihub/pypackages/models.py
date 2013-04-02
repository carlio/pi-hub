from distutils.version import LooseVersion
from urlparse import urljoin
from django.db import models
from django.utils import timezone
from gubbins.db.field import EnumField
from pypackages import pypi
from hashlib import md5



class FetchStatus(EnumField):
    """ An enum to describe whether or not the given model's data has been fetched from PyPI yet or not. """
    NOT_STARTED = 'not_started'
    FETCHING = 'fetching'
    COMPLETE = 'complete'


class PythonPackage(models.Model):
    # named PythonPackage to avoid conflicts with the 'package' keyword...

    name = models.CharField(max_length=100)
    """ The name of this package """

    last_sync = models.DateTimeField(null=True, blank=True)
    """ The last time we ran a check against PyPI for new information """

    fetch_status = FetchStatus(default=FetchStatus.NOT_STARTED)
    """ The status of the fetching of information about this package """


    @property
    def latest_release(self):
        if self.release_set().count() == 0:
            return None
        releases = sort_release_list(self.release_set())
        return releases[0]

    def sync(self):
        releases = pypi.find_all_releases(self.name)
        package_releases = []
        for release in releases:
            obj, created = PackageRelease.objects.get_or_create(python_package=self, version=release)
            package_releases.append( (obj, created) )

        self.last_sync = timezone.now()
        self.save()
        return package_releases

    def __unicode__(self):
        return self.name



class PackageRelease(models.Model):
    """
    Represents an individual release of a particular version of a python package
    """

    python_package = models.ForeignKey(PythonPackage)
    """ The package this is a release of """

    version = models.CharField(max_length=40)
    """ The version of this particular release. While in theory it'd be lovely if they all followed some
        actual standard, it's rather hit-and-miss what can be in here, hence the freeform nature of the field. """

    fetch_status = FetchStatus(default=FetchStatus.NOT_STARTED)
    """ Indicates whether we have pulled the releaese data and URLs for
        this release from PyPI yet """


    def get_pypi_url(self):
        """
        FIXME Needs love. Does awful things. Can't find best thing to use for path component validation, so using optimism...
        """
        BASE_URL = 'http://pypi.python.org/pypi'
        return urljoin(BASE_URL, self.package_name, self.version)

    def __unicode__(self):
        return "%s==%s" % (self.python_package.name, self.version)


def sort_release_list(release_list):
    return sorted(release_list, key=lambda x:LooseVersion(x.version), reverse=True)




class FieldHash(models.Model):
    class Meta:
        abstract = True

    field_hash = models.CharField(max_length=32, unique=True, db_index=True)

    def save(self, force_insert=False, force_update=False, using=None):
        self.field_hash = self.calculate_hash()
        models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using)

    def calculate_hash(self):
        hash_val = md5()
        for field in self._meta.fields:
            if field.name in ('release', 'field_hash'):
                continue
            value = getattr(self, field.name)
            hash_val.update(field.name)
            if value is None:
                continue
            if not isinstance(value, (str, unicode)):
                value = str(value)
            else:
                value = value.encode('utf-8')
            hash_val.update(value)
        return hash_val.hexdigest()



class ReleaseData(FieldHash):

    release = models.OneToOneField(PackageRelease)
    summary = models.TextField(null=True, blank=True)

    name = models.CharField(max_length=200, null=True, blank=True)
    version = models.CharField(max_length=200, null=True, blank=True)
    platform = models.CharField(max_length=200, null=True, blank=True)
    supported_platform = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    home_page = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    author_email = models.CharField(max_length=200, null=True, blank=True)
    license = models.TextField(null=True, blank=True)  #@ReservedAssignment
    classifier = models.CharField(max_length=200, null=True, blank=True)
    download_url = models.CharField(max_length=200, null=True, blank=True)
    requires = models.CharField(max_length=200, null=True, blank=True)
    provides = models.CharField(max_length=200, null=True, blank=True)
    obsoletes = models.CharField(max_length=200, null=True, blank=True)
    maintainer = models.CharField(max_length=200, null=True, blank=True)
    maintainer_email = models.CharField(max_length=200, null=True, blank=True)
    requires_python = models.CharField(max_length=200, null=True, blank=True)
    requires_external = models.CharField(max_length=200, null=True, blank=True)
    requires_dist = models.CharField(max_length=200, null=True, blank=True)
    provides_dist = models.CharField(max_length=200, null=True, blank=True)
    obsoletes_dist = models.CharField(max_length=200, null=True, blank=True)
    project_url = models.CharField(max_length=200, null=True, blank=True)
    docs_url = models.CharField(max_length=200, null=True, blank=True)


    def __unicode__(self):
        return 'Data for %s' % self.release



class ReleaseUrl(FieldHash):
    release = models.ForeignKey(PackageRelease)

    url = models.URLField()
    packagetype = models.CharField(max_length=20)
    filename = models.CharField(max_length=100)
    size = models.IntegerField(null=True, blank=True)
    md5_digest = models.CharField(max_length=32)
    downloads = models.IntegerField(null=True, blank=True)
    has_sig = models.BooleanField()
    python_version = models.CharField(max_length=50)
    comment_text = models.TextField(null=True, blank=True)
    upload_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return 'URL for %s' % self.release
