from tkinter import *
from DataBase import EventDetails
from DataBase import TicketDetails

def ViewEvents():
    
    event_details = EventDetails()[5]
    top4 = Tk()
    top4.geometry('900x500')
    top4.title('VIEW EVENTS')
    top4.configure(bg='#FFFDF4')
    top4.columnconfigure([0,1,2,3,4], weight=1, minsize=100)
    Label(top4, text="Event Name", bg='#FFFDF4', width=20).grid(row=0, column=0, padx=10, pady=10)
    Label(top4, text="Event ID", bg='#FFFDF4', width=20).grid(row=0, column=1, padx=10)
    Label(top4, text="Event Date", bg='#FFFDF4', width=20).grid(row=0, column=2, padx=10)
    Label(top4, text="Event Time(24 hrs)", bg='#FFFDF4', width=20).grid(row=0, column=3, padx=10)
    Label(top4, text="Event Duration(in hrs)", bg='#FFFDF4', width=20).grid(row=0, column=4, padx=10)
    
    Label(top4, text='------------------'*10, bg='#FFFDF4').grid(row=1, column=0, columnspan=5)
    for i in range(len(event_details)):
        Label(top4, text=event_details[i][0], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=0)
        Label(top4, text=event_details[i][1], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=1)
        Label(top4, text=event_details[i][2], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=2)
        Label(top4, text=event_details[i][3], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=3)
        Label(top4, text=event_details[i][4], font=('Arial', 12), bg='#FFFDF4', width=20).grid(row=i+2, column=4)
    
    top4.mainloop()