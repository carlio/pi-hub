from distutils.version import LooseVersion
from django.db import models
from gubbins.db.field import EnumField
from hashlib import md5


class FetchStatus(EnumField):
    NOT_STARTED = 'not_started'
    FETCHING = 'fetching'
    COMPLETE = 'complete'


class MirrorState(models.Model):
    index_fetch_status = FetchStatus(default=FetchStatus.NOT_STARTED)


def get_mirror_state():
    if MirrorState.objects.all().count() == 0:
        return MirrorState.objects.create()
    return MirrorState.objects.all()[0]


class Pkg(models.Model):
    # named Pkg to avoid conflicts with the 'package' keyword...
    name = models.CharField(max_length=100)
    
    # whether or not this package is private (ie, it has been uploaded
    # only to this pihub server) or if it is publicly available on PyPI
    private = models.BooleanField()
    
    # if this is not a private package, this field indicates whether we
    # have pulled the release list from PyPI
    fetch_status = FetchStatus(default=FetchStatus.NOT_STARTED)
    
    def get_pypi_index(self):
        return 'http://pypi.python.org/simple/%s/' % self.name
    
    @property
    def latest_release(self):
        releases = sort_release_list(self.release_set())
        if len(releases) == 0:
            return None
        return releases[0]
    
    def __unicode__(self):
        return self.name
    

class Release(models.Model):
    pkg = models.ForeignKey(Pkg)
    version = models.CharField(max_length=40)
    
    # indicates whether we have pulled the releaese data and URLs for
    # this release from PyPI yet
    fetch_status = FetchStatus(default=FetchStatus.NOT_STARTED)
    
    def __unicode__(self):
        return "%s==%s" % (self.pkg.name, self.version)
    
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
            hash_val.update(str(value))
        return hash_val.hexdigest()
        


class ReleaseData(FieldHash):
    
    release = models.OneToOneField(Release)
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
    license = models.CharField(max_length=200, null=True, blank=True) #@ReservedAssignment
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
    release = models.ForeignKey(Release)
    
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
    