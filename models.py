import peewee as pw

db = pw.SqliteDatabase('event_app.db')

class Events(pw.Model):
	event_name = pw.TextField()

	class Meta:
		database = db

class Participants(pw.Model):
	participant_name = pw.TextField()
	event_details = pw.ForeignKeyField(Events)

	class Meta:
		database = db


db.connect()
db.create_tables([Events, Participants])
