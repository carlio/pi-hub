
from django.db import models
from pihub.packages.metadata import HEADER_META_ALL
import re

class Pkg(models.Model):
    # named Pkg to avoid conflicts with the 'package' keyword...
    name = models.CharField(max_length=100)

class ReleaseData(models.Model):
    pkg = models.ForeignKey(Pkg)
     
    version = models.CharField(max_length=40)
    
    summary = models.TextField(null=True)
    
    def __init__(self, *args, **kwargs):
        super(ReleaseData, self).__init__(*args, **kwargs)
        for metadata_field in HEADER_META_ALL:
            field_name = re.sub('-', '_', metadata_field)
            if field_name in self.fields:
                # don't use the default definition if we have already
                # written something specifically
                continue
            self.fields[field_name] = models.CharField(max_length=200, null=True)


    
class ReleaseUrl(models.Model):
    pass