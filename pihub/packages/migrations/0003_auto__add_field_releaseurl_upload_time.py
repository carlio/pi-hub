# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReleaseUrl.upload_time'
        db.add_column('packages_releaseurl', 'upload_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 5, 30, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReleaseUrl.upload_time'
        db.delete_column('packages_releaseurl', 'upload_time')


    models = {
        'packages.pkg': {
            'Meta': {'object_name': 'Pkg'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'packages.release': {
            'Meta': {'object_name': 'Release'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pkg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Pkg']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'packages.releasedata': {
            'Meta': {'object_name': 'ReleaseData'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'classifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'docs_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'project_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provides': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provides_dist': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Release']"}),
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
            'downloads': ('django.db.models.fields.IntegerField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'has_sig': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'md5_digest': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'packagetype': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'python_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['packages.Release']"}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'upload_time': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['packages']