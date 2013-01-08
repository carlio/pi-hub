from distutils.version import LooseVersion
from django.db import models



class PythonPackage(models.Model):
    # named PythonPackage to avoid conflicts with the 'package' keyword...

    name = models.CharField(max_length=100)

    @property
    def latest_release(self):
        if self.release_set().count() == 0:
            return None
        releases = sort_release_list(self.release_set())
        return releases[0]

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

    def __unicode__(self):
        return "%s==%s" % (self.pkg.name, self.version)


def sort_release_list(release_list):
    return sorted(release_list, key=lambda x:LooseVersion(x.version), reverse=True)