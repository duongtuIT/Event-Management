from tkinter import *

from Book import Book 
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket
if __name__ == "__main__":
    top = Tk()
    top.geometry('500x500')
    top.title('Quản lý sự kiện')
    top.rowconfigure([0,1,2], weight=1, minsize=100)
    top.columnconfigure([0,1], weight=1, minsize=100)

    top.configure(bg='#FFFDF4')
    Button(top, text='Book Tickets', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, "bold"), command=lambda: Book()).grid(row=0, column=0, padx=25, pady=30)
    Button(top, text='Create Event', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, "bold"), command=lambda:CreateEvent()).grid(row=0, column=1, padx=25)
    Button(top, text='View Ticket', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, "bold"), command=lambda:ViewTickets()).grid(row=1, pady=20, column=0, padx=25)
    Button(top, text='View Events', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, 'bold'), command=lambda:ViewEvents()).grid(row=1, column=1, padx=25)
    Button(top, text='Cancel Ticket', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, 'bold'), command=lambda: CancelTicket()).grid(row=2, pady=25, column=0, padx=25)
    Button(top, text='Quit', bg='#FFE6CC', fg='black', bd=5, relief=RIDGE ,width=12, font=('Arial', 18, 'bold'), command=lambda: top.destroy()).grid(row=2, column=1, padx=25)

    top.mainloop()