from peewee import *

db =  MySQLDatabase('business', user='root', password='root',host='localhost', port=3316)

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	username = CharField(primary_key=True)
	password = CharField()
	email = CharField()


if __name__== "__main__":
	db.connect()
	db.create_tables([User],safe=True)