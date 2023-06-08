# Models go here
import peewee
import datetime
from peewee import *
import os.path
my_date_now = datetime.datetime.now()
date_now = my_date_now.strftime("%Y-%m-%d, %H:%M:%S")

# Creates a link to the database. In this way it works on any computer and you can run it in Visual Studio Code.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
db = peewee.SqliteDatabase(db_path)


class BaseModel(peewee.Model):
    class Meta:
        database = db


# MOA: dit stond eerst tussen haakjes: peewee.Model, nu Basemodel.
# Daardoor hoef je niet overal class Meta: database = db te zetten.
class User(BaseModel):
    first_name = peewee.CharField(max_length=30)
    last_name = peewee.CharField(max_length=30)
    address_data = peewee.CharField()
    bank_account_number = peewee.CharField()


class Tag(BaseModel):
    name = peewee.CharField(unique=True, max_length=30)


class Product(BaseModel):
    name = peewee.CharField(max_length=255)
    description = peewee.CharField(max_length=150)
    # tag = peewee.ForeignKeyField(Tag, backref='products')
    price_per_unit = peewee.DecimalField(
        decimal_places=2, auto_round=True, default=0)
    amount_stock = peewee.IntegerField()
    owned_by_user = peewee.ForeignKeyField(User, backref='products')


class ProductTag(BaseModel):
    product = peewee.ForeignKeyField(Product, backref='producttags')
    tag = peewee.ForeignKeyField(Tag, backref='tags')


class Transactionbetsy(BaseModel):
    updated_at = peewee.DateTimeField(default=date_now)
    t_user = peewee.ForeignKeyField(User, backref='transactionsbetsys1')
    t_product = peewee.ForeignKeyField(Product, backref='transactionsbetsys2')
    quantity = peewee.IntegerField()
