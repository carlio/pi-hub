from django.contrib import admin
from pihub.packages.models import Release, Pkg, ReleaseData, ReleaseUrl,\
    MirrorState
from django.conf import settings

class FieldHashAdmin(admin.ModelAdmin):
    readonly_fields = ('field_hash', ) + ( () if settings.ADMIN_EDIT_RELEASE else ('release',) )

class PkgAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
class ReleaseInfoAdmin(FieldHashAdmin):
    search_fields = ('release__pkg__name', )

admin.site.register(Pkg, PkgAdmin)
admin.site.register(Release)
admin.site.register(ReleaseData, ReleaseInfoAdmin)
admin.site.register(ReleaseUrl, ReleaseInfoAdmin)
admin.site.register(MirrorState)