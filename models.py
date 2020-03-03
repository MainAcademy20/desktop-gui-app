from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class Text(BaseModel):
    text = CharField()
