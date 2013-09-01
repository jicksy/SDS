# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Expense'
        db.create_table(u'expenses_expense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salesperson', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profiles.SalesPerson'])),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'expenses', ['Expense'])

        # Adding model 'ExpenseDetail'
        db.create_table(u'expenses_expensedetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('expense', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['expenses.Expense'])),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Institution'])),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('timeStamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'expenses', ['ExpenseDetail'])


    def backwards(self, orm):
        # Deleting model 'Expense'
        db.delete_table(u'expenses_expense')

        # Deleting model 'ExpenseDetail'
        db.delete_table(u'expenses_expensedetail')


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
        u'expenses.expense': {
            'Meta': {'object_name': 'Expense'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'salesperson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_profiles.SalesPerson']"})
        },
        u'expenses.expensedetail': {
            'Meta': {'object_name': 'ExpenseDetail'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'expense': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['expenses.Expense']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Institution']"}),
            'timeStamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'reports.institution': {
            'Meta': {'object_name': 'Institution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'pin_code': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Region']"}),
            'subregion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.SubRegion']"})
        },
        u'reports.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'reports.subregion': {
            'Meta': {'object_name': 'SubRegion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Region']"})
        },
        u'user_profiles.salesperson': {
            'Meta': {'object_name': 'SalesPerson'},
            'contactNumber': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['expenses']