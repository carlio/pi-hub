# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PythonPackage.last_sync'
        db.add_column('pypackages_pythonpackage', 'last_sync',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PythonPackage.last_sync'
        db.delete_column('pypackages_pythonpackage', 'last_sync')


    models = {
        'pypackages.packagerelease': {
            'Meta': {'object_name': 'PackageRelease'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'python_package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pypackages.PythonPackage']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'pypackages.pythonpackage': {
            'Meta': {'object_name': 'PythonPackage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_sync': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pypackages']