# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MirrorState'
        db.create_table('packages_mirrorstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('index_fetch_status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('packages', ['MirrorState'])

        # Adding model 'Pkg'
        db.create_table('packages_pkg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fetch_status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('packages', ['Pkg'])

        # Adding model 'Release'
        db.create_table('packages_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pkg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['packages.Pkg'])),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('fetch_status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('packages', ['Release'])

        # Adding model 'ReleaseData'
        db.create_table('packages_releasedata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32, db_index=True)),
            ('release', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['packages.Release'], unique=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('supported_platform', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('home_page', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('author_email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('classifier', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('download_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('requires', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('provides', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('obsoletes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('maintainer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('maintainer_email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('requires_python', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('requires_external', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('requires_dist', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('provides_dist', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('obsoletes_dist', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('project_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('docs_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('packages', ['ReleaseData'])

        # Adding model 'ReleaseUrl'
        db.create_table('packages_releaseurl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field_hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32, db_index=True)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['packages.Release'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('packagetype', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('md5_digest', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('downloads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('has_sig', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('python_version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comment_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('upload_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('packages', ['ReleaseUrl'])


    def backwards(self, orm):
        # Deleting model 'MirrorState'
        db.delete_table('packages_mirrorstate')

        # Deleting model 'Pkg'
        db.delete_table('packages_pkg')

        # Deleting model 'Release'
        db.delete_table('packages_release')

        # Deleting model 'ReleaseData'
        db.delete_table('packages_releasedata')

        # Deleting model 'ReleaseUrl'
        db.delete_table('packages_releaseurl')


    models = {
        'packages.mirrorstate': {
            'Meta': {'object_name': 'MirrorState'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_fetch_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'packages.pkg': {
            'Meta': {'object_name': 'Pkg'},
            'fetch_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'packages.release': {
            'Meta': {'object_name': 'Release'},
            'fetch_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Pkg']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'packages.releasedata': {
            'Meta': {'object_name': 'ReleaseData'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'classifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'docs_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'field_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'home_page': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'maintainer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'maintainer_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'obsoletes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'obsoletes_dist': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'project_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provides': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provides_dist': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['packages.Release']", 'unique': 'True'}),
            'requires': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'requires_dist': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'requires_external': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'requires_python': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'supported_platform': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'packages.releaseurl': {
            'Meta': {'object_name': 'ReleaseUrl'},
            'comment_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'downloads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'has_sig': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5_digest': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'packagetype': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'python_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Release']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'upload_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['packages']