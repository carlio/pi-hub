from haystack import site, indexes
from pihub.packages.models import Pkg

class PkgIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)

site.register(Pkg)

