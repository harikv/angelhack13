# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ComponentList'
        db.create_table('stack_componentlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('component_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('stack', ['ComponentList'])

        # Adding model 'StackItem'
        db.create_table('stack_stackitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_tag', self.gf('django.db.models.fields.CharField')(default=None, max_length=64, null=True, blank=True)),
            ('item_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=64, null=True, blank=True)),
            ('item_component', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['stack.ComponentList'], null=True, blank=True)),
            ('item_justification', self.gf('django.db.models.fields.CharField')(default=None, max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('stack', ['StackItem'])

        # Adding model 'TechStack'
        db.create_table('stack_techstack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(default=None, max_length=128, null=True, blank=True)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('company_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('company_type_of_application', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('frontend_languages', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('frontend_framework', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('frontend_libraries', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('frontend_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('backend_languages', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('backend_framework', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('backend_libraries', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('backend_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('database', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('database_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('server_os', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('server_configuration', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('server_ram', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('server_nodes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('server_hosting_provider', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('server_description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('stack', ['TechStack'])


    def backwards(self, orm):
        # Deleting model 'ComponentList'
        db.delete_table('stack_componentlist')

        # Deleting model 'StackItem'
        db.delete_table('stack_stackitem')

        # Deleting model 'TechStack'
        db.delete_table('stack_techstack')


    models = {
        'stack.componentlist': {
            'Meta': {'object_name': 'ComponentList'},
            'component_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'stack.stackitem': {
            'Meta': {'object_name': 'StackItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_component': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['stack.ComponentList']", 'null': 'True', 'blank': 'True'}),
            'item_justification': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'item_tag': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'stack.techstack': {
            'Meta': {'object_name': 'TechStack'},
            'backend_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'backend_framework': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'backend_languages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'backend_libraries': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'company_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'company_type_of_application': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'database': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'database_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'frontend_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'frontend_framework': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'frontend_languages': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'frontend_libraries': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server_configuration': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'server_description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'server_hosting_provider': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'server_nodes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'server_os': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'server_ram': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stack']