from django.test import TestCase
from pypackages.models import sort_release_list, PackageRelease

class TestReleases(TestCase):
    
    def test_sorting(self):
        
        def _create_release_list(*versions):
            release_list = []
            for version in versions:
                release_list.append( PackageRelease(version=version) )
            return release_list
        
        def _test( expected, test_data ):
            release_list = _create_release_list(*test_data)
            release_list = sort_release_list(release_list)
            versions = [ r.version for r in release_list ]
            self.assertEqual(expected, versions)
        
        _test( ['1.1.1', '1.1.0', '1.0.0'], ['1.1.0', '1.0.0', '1.1.1'])
        _test( ['2.1', '1.4', '1.0'], ['2.1', '1.0', '1.4'])
        _test( ['1.1a4', '1.1a1'], ['1.1a1', '1.1a4'])
