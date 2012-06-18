from django.contrib import admin
from pihub.packages.models import Release, Pkg, ReleaseData, ReleaseUrl,\
    MirrorState
from django.conf import settings

class FieldHashAdmin(admin.ModelAdmin):
    readonly_fields = ('field_hash', ) + ( () if settings.ADMIN_EDIT_RELEASE else ('release',) )

admin.site.register(Pkg)
admin.site.register(Release)
admin.site.register(ReleaseData, FieldHashAdmin)
admin.site.register(ReleaseUrl, FieldHashAdmin)
admin.site.register(MirrorState)