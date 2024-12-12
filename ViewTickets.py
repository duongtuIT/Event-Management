from tkinter import *
from DataBase import EventDetails
from DataBase import TicketDetails
from main import Main
def ViewTickets():
    top4 = Tk()
    top4.geometry('600x400')
    top4.title('VIEW TICKETS')
    top4.configure(bg='#FFFDF4')
    top4.columnconfigure([0,1,2,3,4], weight=1, minsize=100)
    event_names_list = EventDetails()[0]
    
    event_name = StringVar(top4)
    
    event_name.set('Select event')
    
    def ShowTickets():
        Label(top4, text="Customer Name", bg='#FFFDF4').grid(row=3, column=0, padx=10, pady=10)
        Label(top4, text="Ticket ID", bg='#FFFDF4').grid(row=3, column=1, padx=10, pady=10)
        Label(top4, text="Event Name", bg='#FFFDF4').grid(row=3, column=2, padx=10, pady=10)
        Label(top4, text="Event Date", bg='#FFFDF4').grid(row=3, column=3, padx=10, pady=10)
        required_tickets = []
        for i in TicketDetails()[7]:
            if event_name.get() in i:
                required_tickets.append(i)
        for i in range(len(required_tickets)):
            Label(top4, text=required_tickets[i][0], font=('Arial', 12), bg='#FFFDF4', width=10).grid(row=i+4, column=0)
            Label(top4, text=required_tickets[i][1], font=('Arial', 12), bg='#FFFDF4', width=10).grid(row=i+4, column=1)
            Label(top4, text=required_tickets[i][2], font=('Arial', 12), bg='#FFFDF4', width=10).grid(row=i+4, column=2)
            Label(top4, text=required_tickets[i][4], font=('Arial', 12), bg='#FFFDF4', width=10).grid(row=i+4, column=3)
    
    def Back():
        top4.destroy()
        Main()
    Label(top4, text='Select Event', font=('Arial', 16), bg='#FFFDF4').grid(row=0, column=0, padx=10, sticky='w', pady=10)
    OptionMenu(top4, event_name, *event_names_list).grid(row=0, column=1, columnspan=2, sticky='w')
    
    Button(top4, text='Submit', command=ShowTickets, bg='#6C767D', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=3, sticky='we', padx=10)
    Button(top4, text='Back', command=Back, bg='#F8CECC', fg='black', font=('Arial', 12, 'bold')).grid(row=0, column=4, sticky='we', padx=10)
    top4.mainloop()