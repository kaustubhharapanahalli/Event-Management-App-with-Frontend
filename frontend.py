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
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("750x480")
		self.show_frame(Main)


	def show_frame(self, cont):
		frame=cont(parent=self.container,controller=self)
		frame.grid(row=0,column=0,sticky="nsew")
		frame.tkraise()



class Main(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="Event Management Application", font=LARGE_FONT)
		
		add_events_btn = Button(self, text='Add Events', command=lambda:controller.show_frame(AddEvents))
		see_events_btn = Button(self, text='See Events', command=lambda:controller.show_frame(SeeEvents))
		
		add_participants_btn = Button(self, text='Add Participants', command=lambda:controller.show_frame(AddParticipants))
		see_participants_btn = Button(self, text='See Participants', command=lambda:controller.show_frame(SeeParticipants))
		quit_btn = Button(self, text='Quit', command=self.controller.quit)

		heading_label.grid(row=2, column=5, padx=120,pady=30)
		
		add_events_btn.grid(row=6, column=5, padx=120, pady=10)
		see_events_btn.grid(row=7, column=5, padx=120, pady=10)

		add_participants_btn.grid(row=8, column=5, padx=120, pady=10)
		see_participants_btn.grid(row=9, column=5, padx=120, pady=10)

		quit_btn.grid(row=10, column=5, padx=120, pady=10)



class AddEvents(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		event_label = Label(self, text="Event",font=11)
		self.event_name = Text(self, height=1, width=30)

		add_event_btn = Button(self,text="Add Event",command=self.add_event)		
		back_btn = Button(self,text="Back",command=lambda:controller.show_frame(Main))

		event_label.grid(row=6, column=1, padx=10, pady=10)
		self.event_name.grid(row=6, column=2, padx=10, pady=10)
		add_event_btn.grid(row=8, column=2, padx=60, pady=15)
		back_btn.grid(row=1, column=1, padx=20, pady=20)


	def add_event(self):
		if len(self.event_name.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Add Event')

		else:
			event=self.event_name.get("1.0", "end-1c")
			add_events(event_name=event)



class SeeEvents(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		event_tree=Treeview( self, columns=('#1','#2'))

		event_tree.heading('#1',text='Sl No.')
		event_tree.heading('#2',text='event name')

		event_tree.column('#1',stretch=YES,anchor=CENTER)
		event_tree.column('#2',stretch=YES,anchor=CENTER)

		event_tree.grid(row=10, column=50, padx=10, pady=10, columnspan=2, sticky='nsew')
		event_tree['show']='headings'

		events_list = see_events()

		for event in events_list:
			event_tree.insert("",'end',values=event)

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		back_btn.grid(row=2, column=1, padx=20, pady=20)



class AddParticipants(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		fullname_label=Label(self, text="Full Name",font=11)
		event_label=Label(self, text="Event",font=11)

		see_participants_tree=Treeview( self, columns=('#1','#2'))
		see_participants_tree.heading('#1', text='Sl No.')
		see_participants_tree.heading('#2', text='event name')

		see_participants_tree.column('#1', stretch=YES, anchor=CENTER)
		see_participants_tree.column('#2', stretch=YES, anchor=CENTER)

		see_participants_tree.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky='nsew')
		see_participants_tree['show']='headings'

		events_list = see_events()
		for event in events_list:
			see_participants_tree.insert("",'end',values=event)

		self.fullname=Text(self, height=1, width=30)
		self.event=Text(self, height=1, width=30)

		fullname_label.grid(row=4, column=1, padx=10, pady=10)
		self.fullname.grid(row=4, column=2, padx=10, pady=10)

		event_label.grid(row=8, column=1, padx=10, pady=10)
		self.event.grid(row=8, column=2, padx=10, pady=10)

		add_participant_btn=Button(self,text="Add Participant",command=self.add_participant)
		add_participant_btn.grid(row = 9, column= 1, padx=10, pady=15)

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		back_btn.grid(row =2, column= 1, padx=20, pady=20)


	def add_participant(self):
		if len(self.fullname.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Enter Full Name')

		elif len(self.event.get('1.0','end-1c')) == 0:
			self.popup=messagebox.showwarning('warning','Event')

		else:
			name=self.fullname.get("1.0","end-1c")
			evnt=self.event.get("1.0", "end-1c")

			add_participants(participant_name=name, event_id=evnt)



class SeeParticipants(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller

		self.see_participants_tree=Treeview( self, columns=('#1','#2'))
		self.see_participants_tree.heading('#1',text='name')
		self.see_participants_tree.heading('#2',text='event name')

		self.see_participants_tree.column('#1',stretch=YES,anchor=CENTER)
		self.see_participants_tree.column('#2',stretch=YES,anchor=CENTER)

		self.see_participants_tree.grid(row=10, column=50, padx=10, pady=10, columnspan=2, sticky='nsew')
		self.see_participants_tree['show']='headings'

		participants_list = see_participants()
	
		for participant in participants_list:
			self.see_participants_tree.insert("",'end',values=participant)

		back_btn=Button(self,text="Back",command=lambda:controller.show_frame(Main))
		back_btn.grid(row =9, column= 1, padx=20, pady=20)

FRAMES = (Main, AddParticipants, SeeParticipants, AddEvents, SeeEvents)

app = Event()
app.mainloop()
