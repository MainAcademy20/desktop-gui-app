from peewee import SqliteDatabase, Model, CharField, ForeignKeyField
import logging

logging.basicConfig(level=logging.DEBUG)

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class List(BaseModel):
    name = CharField()


class Text(BaseModel):
    list_ = ForeignKeyField(List, related_name='texts')
    text = CharField()
