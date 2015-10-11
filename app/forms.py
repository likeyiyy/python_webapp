#!/usr/bin/env python
# coding=utf-8

from flask.ext.wtf import Form
from wtforms import IntegerField,SelectField
from wtforms.validators import DataRequired

class TestForm(Form):
    generator = IntegerField(u'generator',validators = [DataRequired()])
    parser    = IntegerField(u'parser',   validators = [DataRequired()])
    manager   = IntegerField(u'manager',  validators = [DataRequired()])
    pktlen    = IntegerField(u'pktlen',   validators = [DataRequired()])
    gener_pool_sizes     = IntegerField(u'gener_pool_sizes',   validators = [DataRequired()])
    parser_queue_sizes   = IntegerField(u'parser_queue_sizes',   validators = [DataRequired()])
    parser_pool_sizes    = IntegerField(u'parser_pool_sizes',   validators = [DataRequired()])
    manager_queue_sizes  = IntegerField(u'manager_queue_sizes',   validators = [DataRequired()])
    manager_pool_sizes   = IntegerField(u'manager_pool_sizes',   validators = [DataRequired()])
    manager_hash_sizes   = IntegerField(u'manager_hash_sizes',   validators = [DataRequired()])
    manager_buffer_sizes = IntegerField(u'manager_buffer_sizes',   validators = [DataRequired()])
    packet_gener_mode    = IntegerField(u'packet_gener_mode',   validators = [DataRequired()])
    pipe_depth= SelectField(u'pipe_depth',choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')], coerce=int)


