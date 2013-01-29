from __future__ import absolute_import
import logging
import os
from urlparse import urljoin, urlparse
from pyquery import PyQuery as pq
import re


PYPI_INDEX = 'http://pypi.python.org/simple/'


def _package_url(package_name):
    # the case is not important because pypi (at least, the main one) is not case sensitive
    return urljoin(PYPI_INDEX, package_name)


def find_all_releases(package_name):
    # TODO: use requests to open URLs
    package_page = pq(url=_package_url(package_name))
    return _find_releases_on_page(package_name, package_page)


def _find_releases_on_page(package_name, package_page):
    releases = set()

    for anchor in package_page.find('a'):
        href = pq(anchor).attr('href')

        # find the ones which are hosted elsewhere
        if pq(anchor).attr('rel') == 'download':
            # we have to get the version number from the link text
            #   2.7.0 download_url
            linktext = pq(anchor).text()
            version = re.sub(' download_url', '', linktext).strip()
            releases.add(version)
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
                releases.add(version)

    return releases
