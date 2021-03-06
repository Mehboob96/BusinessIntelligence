from peewee import *

db =  MySQLDatabase('business', user='root', password='root',host='localhost', port=3306)

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	username = CharField(primary_key=True)
	password = CharField()
	email = CharField()
	category = CharField()

class Profile(BaseModel):
	username = CharField(primary_key=True)
	funding = BigIntegerField()
	date = CharField()
	fburl = CharField()
	linkedinurl = CharField()
	twitterurl = CharField()
	website = CharField()


if __name__== "__main__":
	db.connect()
	db.create_tables([User],safe=True)
	db.create_tables([Profile],safe=True)
