# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pkg'
        db.create_table('packages_pkg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('packages', ['Pkg'])

        # Adding model 'ReleaseData'
        db.create_table('packages_releasedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pkg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['packages.Pkg'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('packages', ['ReleaseData'])

        # Adding model 'ReleaseUrl'
        db.create_table('packages_releaseurl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('packages', ['ReleaseUrl'])


    def backwards(self, orm):
        # Deleting model 'Pkg'
        db.delete_table('packages_pkg')

        # Deleting model 'ReleaseData'
        db.delete_table('packages_releasedata')

        # Deleting model 'ReleaseUrl'
        db.delete_table('packages_releaseurl')


    models = {
        'packages.pkg': {
            'Meta': {'object_name': 'Pkg'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'packages.releasedata': {
            'Meta': {'object_name': 'ReleaseData'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Pkg']"}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'packages.releaseurl': {
            'Meta': {'object_name': 'ReleaseUrl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['packages']