from tkinter import *

from Book import Book 
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket

top = Tk()
top.geometry('415x450')
top.title('Event Management: CopyAssignment')

Button(top, text='Book Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: Book()).grid(row=0, column=0, padx=25, pady=30)
Button(top, text='Create Event', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:CreateEvent()).grid(row=0, column=1)
Button(top, text='View Tickets', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:ViewTickets()).grid(row=1, pady=20, column=0)
Button(top, text='View Events', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:ViewEvents()).grid(row=1, column=1)
Button(top, text='Cancel Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: CancelTicket()).grid(row=2, pady=25, column=0)
Button(top, text='Quit App', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: top.destroy()).grid(row=2, column=1)

Label(top, text='Thank you for choosing\nCopyAssignment', font=('Arial', 24)).grid(row=3, column=0, columnspan=2)
top.mainloop()