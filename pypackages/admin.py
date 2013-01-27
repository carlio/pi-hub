from django.contrib import admin
from pypackages.models import PythonPackage, PackageRelease

class PackageReleaseInline(admin.TabularInline):
    model = PackageRelease


def sync_package(modeladmin, request, queryset):
    for pkg in queryset:
        pkg.sync()
sync_package.short_description = "Sync selected packages"


class PythonPackageAdmin(admin.ModelAdmin):
    inlines = [PackageReleaseInline]
    readonly_fields = ('last_sync',)
    actions = [ sync_package ]


admin.site.register(PythonPackage, PythonPackageAdmin)