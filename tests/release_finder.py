# -*- coding: UTF-8 -*-

import os
from pyquery import PyQuery as pq
from django.test import TestCase
from pypackages.models import PythonPackage
from pypackages.pypi import PackageFinder


class PackageFinderTest(TestCase):

    def _get_file(self, filename):
        here = os.path.abspath(__file__)
        filepath = os.path.join( os.path.dirname(here), 'testdata', filename )
        with open(filepath) as f:
            return f.read()

    def test_find_all_redis_releases(self):
        expected_releases = [
            '2.7.2', '2.7.1', '2.7.0',
            '2.4.3', '2.4.10', '2.2.1', '2.4.8', '2.4.6', '2.4.13', '2.4.11', '1.34', '2.2.4', '2.2.2',
            '2.0.0', '2.4.12', '2.6.2', '2.6.1', '2.4.2', '1.34.1', '2.2.0', '0.6.0', '2.4.7', '2.4.4', '2.4.0',
            '2.4.5', '2.4.1', '2.6.0', '2.4.9', '0.6.1'
        ]

        self._test_find_releases('redis', expected_releases)


    def test_find_unicode_snowman_releases(self):
        self._test_find_releases('☃', [])


    def test_find_all_django_releases(self):
        expected_releases = ['1.4', '1.0.4', '1.1.3', '1.1.2', '1.1.4', '1.2', '1.3', '1.3.4', '1.1', '1.0.2', '1.0.3',
                             '1.1.1', '1.4.1', '1.4.2', '1.4.3', '1.2.6', '1.3.2', '1.2.4', '1.2.5', '1.2.2', '1.2.3',
                             '1.3.5', '1.2.1', '1.3.3', '1.2.7', '1.3.1', '1.0.1']

        self._test_find_releases('django', expected_releases)


    def _test_find_releases(self, package_name, expected_releases):

        pkg = PythonPackage.objects.create(name=package_name)

        html = self._get_file('%s.html' % package_name)
        page = pq(html)

        releases = PackageFinder()._find_releases_on_page(pkg, page)

        for release in releases:
            self.assertIn( release.version, expected_releases )

        # at this point, we could just check the lists have equivalent length to ensure they are equal, however
        # it is easier for debugging to get an explicit message
        release_versions = [ r.version for r in releases ]
        for release in expected_releases:
            self.assertIn( release, release_versions )

        self.assertEqual( len(expected_releases), len(releases) )
