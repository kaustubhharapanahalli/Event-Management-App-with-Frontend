from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from PIL import Image, ImageTk

from views import add_events, add_participants, see_events, see_participants

LARGE_FONT=("Verdana",24)
MED_FONT=("Verdana",18)

class Event(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		Tk.configure(self)
		
		container=Frame(self)

		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
			
		self.geometry("720x480")
	
		self.frames={}

		for frm in FRAMES:
			frame=frm(parent=container,controller=self)
			self.frames[frm]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(Main)

		print(self.frames)

	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


class Main(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Event Management Application", font=LARGE_FONT)
		label.grid(row=2, column=5, padx=120,pady=30)
		
		button1 = Button(self, text = 'Add Events', command = lambda:controller.show_frame(AddEvents))
		button1.grid(row=6, column=5, padx = 120, pady=10)
		button1 = Button(self, text = 'See Events', command = lambda:controller.show_frame(SeeEvents))
		button1.grid(row=7, column=5, padx = 120, pady=10)
		button1 = Button(self, text = 'Add Participants', command = lambda:controller.show_frame(AddParticipants))
		button1.grid(row=8, column=5, padx = 120, pady=10)
		button1 = Button(self, text = 'See Participants', command = lambda:controller.show_frame(SeeParticipants))
		button1.grid(row=9, column=5, padx = 120, pady=10)


class AddEvents(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.event_label=Label(self, text="Event",font=11)

		self.event_name=Text(self, height=1, width=30)

		self.event_label.grid(row=6, column=1, padx=10, pady=10)
		self.event_name.grid(row=7, column=1, padx=10, pady=10)

		button2=Button(self,text="Add Event",command=self.add_event)
		button2.grid(row = 8, column = 1, padx = 10, pady = 15)

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =9, column = 1, padx=20, pady =20)

	def add_event(self):
		if len(self.event_name.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Event')

		else:
			self.event=self.event_name.get("1.0", "end-1c")

			print(self.event)

			add_events(event_name=self.event)


class SeeEvents(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.tree1=Treeview( self, columns=('#1','#2'))
		self.tree1.heading('#1',text='Sl No.')
		self.tree1.heading('#2',text='event name')

		self.tree1.column('#1',stretch=YES,anchor=CENTER)
		self.tree1.column('#2',stretch=YES,anchor=CENTER)

		self.tree1.grid(row=10, column=50, padx=10, pady=10, columnspan=2, sticky='nsew')
		self.tree1['show']='headings'

		events_list = see_events()
		print(events_list)

		for event in events_list:
			self.tree1.insert("",'end',values=event)

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =9, column = 1, padx=20, pady =20)


class AddParticipants(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.fullname_label=Label(self, text="Full Name",font=11)
		self.event_label=Label(self, text="Event",font=11)

		self.tree1=Treeview( self, columns=('#1','#2'))
		self.tree1.heading('#1',text='Sl No.')
		self.tree1.heading('#2',text='event name')

		self.tree1.column('#1',stretch=YES,anchor=CENTER)
		self.tree1.column('#2',stretch=YES,anchor=CENTER)

		self.tree1.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky='nsew')
		self.tree1['show']='headings'

		events_list = see_events()
		print(events_list)

		for event in events_list:
			self.tree1.insert("",'end',values=event)

		self.fullname=Text(self, height=1, width=30)
		self.event=Text(self, height=1, width=30)

		self.fullname_label.grid(row=4, column=1, padx=10, pady=10)
		self.fullname.grid(row=4, column=2, padx=10, pady=10)
		self.event_label.grid(row=8, column=1, padx=10, pady=10)
		self.event.grid(row=8, column=2, padx=10, pady=10)

		button2=Button(self,text="Add Participant",command=self.add_participant)
		button2.grid(row = 9, column = 1, padx = 10, pady = 15)

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =2, column = 1, padx=20, pady =20)

	def add_participant(self):
		if len(self.fullname.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Full Name')

		elif len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Event')

		else:
			self.name=self.fullname.get("1.0","end-1c")
			self.evnt=self.event.get("1.0", "end-1c")

			print(self.name, self.evnt)

			add_participants(participant_name=self.name, event_id=self.evnt)


class SeeParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.tree1=Treeview( self, columns=('#1','#2'))
		self.tree1.heading('#1',text='name')
		self.tree1.heading('#2',text='event name')

		self.tree1.column('#1',stretch=YES,anchor=CENTER)
		self.tree1.column('#2',stretch=YES,anchor=CENTER)

		self.tree1.grid(row=10, column=50, padx=10, pady=10, columnspan=2, sticky='nsew')
		self.tree1['show']='headings'

		participants_list = see_participants()
	
		for participant in participants_list:
			self.tree1.insert("",'end',values=participant)

		button1=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		button1.grid(row =9, column = 1, padx=20, pady =20)

FRAMES = (Main, AddParticipants, SeeParticipants, AddEvents, SeeEvents)

app = Event()
app.mainloop()
