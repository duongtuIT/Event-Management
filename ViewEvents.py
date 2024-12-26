from tkinter import *
from DataBase import EventDetails
from DataBase import TicketDetails
from main import Main
from datetime import datetime
def ViewEvents():
    
    event_details = EventDetails()[5]
    top4 = Tk()
    top4.geometry('1100x500')
    top4.title('VIEW EVENTS')
    top4.configure(bg='#FFFDF4')
    top4.columnconfigure([0,1,2,3,4,5], weight=1, minsize=100)
    def Back():
        top4.destroy()
        Main()
    Button(top4, text='Back', fg='black', bg='#F8CECC', command=Back, width=12, font=('Arial', 10, 'bold')).grid(row=0, column=0, pady=5, padx=10)
    Label(top4, text="Event Name", bg='#FFFDF4', width=20, font=('Arial', 12, 'bold')).grid(row=0, column=1, padx=10, pady=10)
    Label(top4, text="Event ID", bg='#FFFDF4', width=20, font=('Arial', 12, 'bold')).grid(row=0, column=2, padx=10)
    Label(top4, text="Event Date", bg='#FFFDF4', width=20, font=('Arial', 12, 'bold')).grid(row=0, column=3, padx=10)
    Label(top4, text="Event Time(24 hrs)", bg='#FFFDF4', width=20, font=('Arial', 12, 'bold')).grid(row=0, column=4, padx=10)
    Label(top4, text="Event Duration(in hrs)", bg='#FFFDF4', width=20, font=('Arial', 12, 'bold')).grid(row=0, column=5, padx=10)
    
    
    for i in range(len(event_details)):
        event_date = event_details[i][2]
        
        try:
           formatted_date = datetime.strptime(str(event_date), "%Y-%m-%d").strftime("%d/%m/%Y")

        except ValueError:
            formatted_date = event_date
        
        Label(top4, text=event_details[i][0], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=1)
        Label(top4, text=event_details[i][1], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=2)
        Label(top4, text=formatted_date, font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=3)
        Label(top4, text=event_details[i][3], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=4)
        Label(top4, text=event_details[i][4], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=5)
    
    top4.mainloop()