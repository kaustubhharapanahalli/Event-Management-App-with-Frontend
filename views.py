from models import *

def add_events(event_name):
	Events.create(event_name=event_name)


def see_events():
	events = []
	for event in Events.select():
		print(event.id, event.event_name, sep=" | ")
		events.append([event.id, event.event_name])
	print(events)

	return events


def add_participants(participant_name, event_id):
	events = Events.select()
	for event in events:
		print(event.id, event.event_name, sep=" - ")

	Participants.create(participant_name=participant_name, event_details=event_id)


def see_participants():
	participants = []
	for participant in Participants.select():
		print(participant.participant_name, Events.get(participant.event_details_id).event_name, sep=" | ")
		participants.append([participant.participant_name, Events.get(participant.event_details_id).event_name])
	print(participants)

	return participants
