from tkinter import *
from DataBase import TicketDetails
from DataBase import DeleteTicket
from Message import show_message, show_message2
from main import Main
from tkinter import messagebox
def CancelTicket():
    top3 = Tk()
    top3.geometry('790x500')
    top3.title('CANCEL TICKET')
    top3.configure(bg='#FFFDF4')
    top3.columnconfigure([0,1,2,3,4], weight=1, minsize=100)
    def Back():
        top3.destroy()
        Main()
    Label(top3, text='Customer Name', font=('Arial', 12, 'bold'), width=20, bg='#FFFDF4').grid(row=0, column=0, pady=10)
    Label(top3, text='Ticket ID', font=('Arial', 12, 'bold'),  width=20, bg='#FFFDF4').grid(row=0, column=1, pady=10)
    Label(top3, text='Event Name', font=('Arial', 12, 'bold'), width=20, bg='#FFFDF4').grid(row=0, column=2, pady=10)
    Label(top3, text='Event Date', font=('Arial', 12, 'bold'), width=20, bg='#FFFDF4').grid(row=0, column=3, pady=10)
    Button(top3, text='Back', fg='black', bg='#F8CECC', command=Back, width=12, font=('Arial', 10, 'bold')).grid(row=0, column=4, pady=5, padx=10)
    Label(top3, text='------------------'*10, bg='#FFFDF4').grid(row=1, column=0, columnspan=5)
    def delete_rows(ticket_id):
        result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this ticket?")
        if result:
            delete_status = DeleteTicket(ticket_id)
            if delete_status == 'Success':
                show_message('Success', 'Ticket deleted successfully')
                # Hiển thị danh sách vé ban đầu
                update_ticket_list()
            else:
                show_message2('Error', delete_status)
                return
    
    for i in range(len(TicketDetails()[7])):
        Label(top3, text=TicketDetails()[7][i][0], width=20, bg='#FFFDF4').grid(row=i+2,  column=0)
        Label(top3, text=TicketDetails()[7][i][1], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=1)
        Label(top3, text=TicketDetails()[7][i][2], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=2)
        Label(top3, text=TicketDetails()[7][i][4], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=3)
        Button(top3, text='Delete', fg='black', bg='#F8CECC', command=lambda current_id=TicketDetails()[7][i][1]: delete_rows(current_id)).grid(row=i+2, column=4, pady=5)
    def update_ticket_list():
        # Xóa các label cũ trước khi cập nhật lại danh sách vé
        for widget in top3.winfo_children():
            if isinstance(widget, Label) or isinstance(widget, Button):
                if widget.grid_info().get('row') > 1:
                    widget.grid_forget()

        # Hiển thị lại danh sách vé mới
        for i in range(len(TicketDetails()[7])):
            Label(top3, text=TicketDetails()[7][i][0], width=20, bg='#FFFDF4').grid(row=i+2,  column=0)
            Label(top3, text=TicketDetails()[7][i][1], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=1)
            Label(top3, text=TicketDetails()[7][i][2], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=2)
            Label(top3, text=TicketDetails()[7][i][4], width=20, bg='#FFFDF4').grid(row=i+2,  padx=10, column=3)
            Button(top3, text='Delete', fg='black', bg='#F8CECC', command=lambda current_id=TicketDetails()[7][i][1]: delete_rows(current_id)).grid(row=i+2, column=4, pady=5)

    
    top3.mainloop()