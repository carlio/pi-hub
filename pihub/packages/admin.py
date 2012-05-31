from django.contrib import admin
from pihub.packages.models import Release, Pkg, ReleaseData, ReleaseUrl

admin.site.register(Pkg)
admin.site.register(Release)
admin.site.register(ReleaseData)
admin.site.register(ReleaseUrl)