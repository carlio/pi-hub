# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        
        query = """
        update packages_releasedata set field_hash=
        md5(concat("summary", packages_releasedata.summary,"name", packages_releasedata.name,"version", 
        packages_releasedata.version,"platform", packages_releasedata.platform,"supported_platform", 
        packages_releasedata.supported_platform,"description", packages_releasedata.description,"keywords",
        packages_releasedata.keywords,"home_page", packages_releasedata.home_page,"author", 
        packages_releasedata.author,"author_email", packages_releasedata.author_email,"license", 
        packages_releasedata.license,"classifier", packages_releasedata.classifier,"download_url", 
        packages_releasedata.download_url,"requires", packages_releasedata.requires,"provides", 
        packages_releasedata.provides,"obsoletes", packages_releasedata.obsoletes,"maintainer", 
        packages_releasedata.maintainer,"maintainer_email", packages_releasedata.maintainer_email,
        "requires_python", packages_releasedata.requires_python,"requires_external", 
        packages_releasedata.requires_external,"requires_dist", packages_releasedata.requires_dist,"provides_dist", 
        packages_releasedata.provides_dist,"obsoletes_dist", packages_releasedata.obsoletes_dist,"project_url", 
        packages_releasedata.project_url,"docs_url", packages_releasedata.docs_url))
        """
        db.execute(query)

    def backwards(self, orm):
        pass
    
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
            'field_hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
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
    symmetrical = True