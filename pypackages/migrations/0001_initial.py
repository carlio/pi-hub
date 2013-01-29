# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PythonPackage'
        db.create_table('pypackages_pythonpackage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('pypackages', ['PythonPackage'])

        # Adding model 'PackageRelease'
        db.create_table('pypackages_packagerelease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('python_package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pypackages.PythonPackage'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('pypackages', ['PackageRelease'])


    def backwards(self, orm):
        # Deleting model 'PythonPackage'
        db.delete_table('pypackages_pythonpackage')

        # Deleting model 'PackageRelease'
        db.delete_table('pypackages_packagerelease')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['pypackages']