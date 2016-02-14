#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')

baza = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = baza


class TextToDisplay(BaseModel):
    text1 = CharField(default='')
    text2 = CharField(default='')
    text3 = CharField(default='')
    id = IntegerField()


baza.connect()
baza.create_tables([TextToDisplay], True)

texts = [
         {'text1': 'To jest przykladowy tekst dla id 8289', 'text2': 'Tekst drugi', 'text3': 'Trzeci tekst', 'id': 8289},
         {'text1': 'Tekst1 dla id 897', 'text2': 'Tekst 2', 'text3': 'Tekst 3', 'id': 897},
         {'text1': 'Tekst dla id 5', 'text2': 'Kolejny', 'id': 5}
]

TextToDisplay.insert_many(texts).execute()