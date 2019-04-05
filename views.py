from models import *

def add_events(event_name):
	Events.create(event_name=event_name)


def see_events():
	events = []
	for event in Events.select():
		events.append([event.id, event.event_name])

	return events


def add_participants(participant_name, event_id):
	Participants.create(participant_name=participant_name, event_details=event_id)


def see_participants():
	participants = []
	for participant in Participants.select():
		participants.append([participant.participant_name, Events.get(participant.event_details_id).event_name])

	return participants
