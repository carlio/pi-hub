
from django.db import models
from pihub.packages.metadata import HEADER_META_ALL
import re

class Pkg(models.Model):
    # named Pkg to avoid conflicts with the 'package' keyword...
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    

class Release(models.Model):
    pkg = models.ForeignKey(Pkg)
    version = models.CharField(max_length=40)
    
    def __unicode__(self):
        return "%s==%s" % (self.pkg.name, self.version)
    

class ReleaseData(models.Model):
    
    release = models.ForeignKey(Release)
    summary = models.TextField(null=True, blank=True)
    
    metadata_version = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    version = models.CharField(max_length=200, null=True, blank=True)
    platform = models.CharField(max_length=200, null=True, blank=True)
    supported_platform = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    home_page = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    author_email = models.CharField(max_length=200, null=True, blank=True)
    license = models.CharField(max_length=200, null=True, blank=True)
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

    def __unicode__(self):
        return 'Data for %s' % self.release


    
class ReleaseUrl(models.Model):
    release = models.ForeignKey(Release)
    
    url = models.URLField()
    packagetype = models.CharField(max_length=20)
    filename = models.CharField(max_length=100)
    size = models.IntegerField()
    md5_digest = models.CharField(max_length=32)
    downloads = models.IntegerField()
    has_sig = models.BooleanField()
    python_version = models.CharField(max_length=50)
    comment_text = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return 'URL for %s' % self.release
    