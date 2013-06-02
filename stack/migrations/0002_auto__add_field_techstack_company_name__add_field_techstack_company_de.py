# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TechStack.company_name'
        db.add_column('stack_techstack', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.company_description'
        db.add_column('stack_techstack', 'company_description',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.company_type_of_application'
        db.add_column('stack_techstack', 'company_type_of_application',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.frontend_languages'
        db.add_column('stack_techstack', 'frontend_languages',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.frontend_framework'
        db.add_column('stack_techstack', 'frontend_framework',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.frontend_libraries'
        db.add_column('stack_techstack', 'frontend_libraries',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.frontend_description'
        db.add_column('stack_techstack', 'frontend_description',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.backend_languages'
        db.add_column('stack_techstack', 'backend_languages',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.backend_framework'
        db.add_column('stack_techstack', 'backend_framework',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.backend_libraries'
        db.add_column('stack_techstack', 'backend_libraries',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.backend_description'
        db.add_column('stack_techstack', 'backend_description',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.database'
        db.add_column('stack_techstack', 'database',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.database_description'
        db.add_column('stack_techstack', 'database_description',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_os'
        db.add_column('stack_techstack', 'server_os',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_configuration'
        db.add_column('stack_techstack', 'server_configuration',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_ram'
        db.add_column('stack_techstack', 'server_ram',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_nodes'
        db.add_column('stack_techstack', 'server_nodes',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_hosting_provider'
        db.add_column('stack_techstack', 'server_hosting_provider',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'TechStack.server_description'
        db.add_column('stack_techstack', 'server_description',
                      self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TechStack.company_name'
        db.delete_column('stack_techstack', 'company_name')

        # Deleting field 'TechStack.company_description'
        db.delete_column('stack_techstack', 'company_description')

        # Deleting field 'TechStack.company_type_of_application'
        db.delete_column('stack_techstack', 'company_type_of_application')

        # Deleting field 'TechStack.frontend_languages'
        db.delete_column('stack_techstack', 'frontend_languages')

        # Deleting field 'TechStack.frontend_framework'
        db.delete_column('stack_techstack', 'frontend_framework')

        # Deleting field 'TechStack.frontend_libraries'
        db.delete_column('stack_techstack', 'frontend_libraries')

        # Deleting field 'TechStack.frontend_description'
        db.delete_column('stack_techstack', 'frontend_description')

        # Deleting field 'TechStack.backend_languages'
        db.delete_column('stack_techstack', 'backend_languages')

        # Deleting field 'TechStack.backend_framework'
        db.delete_column('stack_techstack', 'backend_framework')

        # Deleting field 'TechStack.backend_libraries'
        db.delete_column('stack_techstack', 'backend_libraries')

        # Deleting field 'TechStack.backend_description'
        db.delete_column('stack_techstack', 'backend_description')

        # Deleting field 'TechStack.database'
        db.delete_column('stack_techstack', 'database')

        # Deleting field 'TechStack.database_description'
        db.delete_column('stack_techstack', 'database_description')

        # Deleting field 'TechStack.server_os'
        db.delete_column('stack_techstack', 'server_os')

        # Deleting field 'TechStack.server_configuration'
        db.delete_column('stack_techstack', 'server_configuration')

        # Deleting field 'TechStack.server_ram'
        db.delete_column('stack_techstack', 'server_ram')

        # Deleting field 'TechStack.server_nodes'
        db.delete_column('stack_techstack', 'server_nodes')

        # Deleting field 'TechStack.server_hosting_provider'
        db.delete_column('stack_techstack', 'server_hosting_provider')

        # Deleting field 'TechStack.server_description'
        db.delete_column('stack_techstack', 'server_description')


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
            'server_ram': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stack_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'tech_stack'", 'null': 'True', 'blank': 'True', 'to': "orm['stack.StackItem']"})
        }
    }

    complete_apps = ['stack']