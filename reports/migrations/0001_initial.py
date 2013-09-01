# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'reports_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'reports', ['Region'])

        # Adding model 'SubRegion'
        db.create_table(u'reports_subregion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Region'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'reports', ['SubRegion'])

        # Adding model 'Institution'
        db.create_table(u'reports_institution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Region'])),
            ('subregion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.SubRegion'])),
            ('pin_code', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'reports', ['Institution'])

        # Adding model 'InstitutionStaff'
        db.create_table(u'reports_institutionstaff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
        ))
        db.send_create_signal(u'reports', ['InstitutionStaff'])

        # Adding model 'ItemCategory'
        db.create_table(u'reports_itemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'reports', ['ItemCategory'])

        # Adding model 'Item'
        db.create_table(u'reports_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.ItemCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'reports', ['Item'])

        # Adding model 'Report'
        db.create_table(u'reports_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('meeting_note', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('stage_of_negotiation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding model 'InstitutionPurchase'
        db.create_table(u'reports_institutionpurchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('sale_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Item'])),
            ('sale_count', self.gf('django.db.models.fields.IntegerField')()),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'reports', ['InstitutionPurchase'])

        # Adding model 'InstitutionFurtherPurchase'
        db.create_table(u'reports_institutionfurtherpurchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('scope_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Item'])),
            ('scope_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'reports', ['InstitutionFurtherPurchase'])

        # Adding model 'Visit'
        db.create_table(u'reports_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'reports', ['Visit'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'reports_region')

        # Deleting model 'SubRegion'
        db.delete_table(u'reports_subregion')

        # Deleting model 'Institution'
        db.delete_table(u'reports_institution')

        # Deleting model 'InstitutionStaff'
        db.delete_table(u'reports_institutionstaff')

        # Deleting model 'ItemCategory'
        db.delete_table(u'reports_itemcategory')

        # Deleting model 'Item'
        db.delete_table(u'reports_item')

        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Deleting model 'InstitutionPurchase'
        db.delete_table(u'reports_institutionpurchase')

        # Deleting model 'InstitutionFurtherPurchase'
        db.delete_table(u'reports_institutionfurtherpurchase')

        # Deleting model 'Visit'
        db.delete_table(u'reports_visit')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'reports.institution': {
            'Meta': {'object_name': 'Institution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'pin_code': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Region']"}),
            'subregion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.SubRegion']"})
        },
        u'reports.institutionfurtherpurchase': {
            'Meta': {'object_name': 'InstitutionFurtherPurchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'scope_count': ('django.db.models.fields.IntegerField', [], {}),
            'scope_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Item']"})
        },
        u'reports.institutionpurchase': {
            'Meta': {'object_name': 'InstitutionPurchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"}),
            'sale_count': ('django.db.models.fields.IntegerField', [], {}),
            'sale_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Item']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'reports.institutionstaff': {
            'Meta': {'object_name': 'InstitutionStaff'},
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'reports.item': {
            'Meta': {'object_name': 'Item'},
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.ItemCategory']"})
        },
        u'reports.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'reports.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'reports.report': {
            'Meta': {'object_name': 'Report'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'meeting_note': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'stage_of_negotiation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'reports.subregion': {
            'Meta': {'object_name': 'SubRegion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Region']"})
        },
        u'reports.visit': {
            'Meta': {'object_name': 'Visit'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['reports']