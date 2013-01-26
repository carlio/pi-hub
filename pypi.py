from __future__ import absolute_import
import logging
import os
from urlparse import urljoin, urlparse
from pyquery import PyQuery as pq
import re
from pypackages.models import PackageRelease


PYPI_INDEX = 'http://pypi.python.org/simple/'



class PackageFinder(object):

    def __init__(self, index_url=None):
        self.index_url = index_url or PYPI_INDEX


    def _package_url(self, python_package):
        # the case is not important because pypi (at least, the main one) is not case sensitive
        return urljoin(self.index_url, python_package.name)


    def find_all_releases(self, python_package):
        # TODO: use requests to open URLs
        package_page = pq(url=self._package_url(python_package))
        return self._find_releases_on_page(python_package, package_page)


    def _find_releases_on_page(self, python_package, package_page):
        package_name = python_package.name
        releases = {}

        for anchor in package_page.find('a'):
            href = pq(anchor).attr('href')

            # find the ones which are hosted elsewhere
            if pq(anchor).attr('rel') == 'download':
                # we have to get the version number from the link text
                #   2.7.0 download_url
                linktext = pq(anchor).text()
                version = re.sub(' download_url', '', linktext).strip()
                releases[version] = PackageRelease(python_package, version=version)
                continue

            # the rest are hosted on pypi
            parts = urlparse(href)
            for ext in ('.tar', '.tar.gz', '.tar.bz2', '.tgz', '.zip'):
                if parts.path.endswith(ext):
                    filename = os.path.basename(parts.path)
                    if not filename.lower().startswith(package_name.lower()):
                        # we currently assume that all useful downloads on this page will be of the form
                        # packagename-version.ext
                        logging.warning("Unexpected package filename format: %s for package %s" % (filename, package_name))
                        continue

                    # strip the package name and the extension
                    # note we use len(package_name)+1 to include the leading hyphen, eg, 'Django-]1.2.3[.tar.gz'
                    version = filename[len(package_name)+1 : -len(ext)]
                    releases[version] = PackageRelease(python_package=python_package, version=version)

        return list(releases.values())
