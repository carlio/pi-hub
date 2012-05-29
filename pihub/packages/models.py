
from django.db import models

class Pkg(models.Model):
    # named Pkg to avoid conflicts with the 'package' keyword...
    pass

class ReleaseData(models.Model):
    pkg = models.ForeignKey(Pkg)
     
    version = models.CharField(max_length=40)
    
class ReleaseUrl(models.Model):
    pass