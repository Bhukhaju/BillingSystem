from tkinter import *
from classes.Connection import Connector


class Bill_Generate:

    def __init__(self, invoice_number):
        self.db = Connector()
        self.__query = self.db.my_cursor

        # Create window object
        self.window = Tk()

        self.window.title('Bill Generate')
        self.window.geometry('650x600')

        self.invoice_number = invoice_number
        self.bill_details = ''


        # Bill_System
        self.bill_system = Label(self.window, text='Bill System', font=('bold', 14))
        self.bill_system.place(x=260, y=20)

        # Frame
        self.bill_generate = Frame(self.window, bd=5, relief=RIDGE)
        self.bill_generate.place(x=15, y=15, width=620, height=575)

        self.scrol_y = Scrollbar(self.bill_generate, orient=VERTICAL)
        self.txtarea = Text(self.bill_generate,yscrollcommand=self.scrol_y.set)
        self.scrol_y.pack(side=RIGHT, fill=Y)
        self.scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        self.get_bill_details()
        self.bill_view()

    def bill_view(self):
        grand_total = 0
        self.txtarea.insert(END,"\t\t\t\tWelcome")
        self.txtarea.insert(END, "\nInvoice Number: "+str(self.invoice_number))
        self.txtarea.insert(END, "\nCustomer Name: "+str(self.bill_details[0][5]))
        self.txtarea.insert(END, "\nAddress: "+str(self.bill_details[0][6]))
        self.txtarea.insert(END, "\nPhone Number: "+str(self.bill_details[0][0]))
        self.txtarea.insert(END, "\nDate: "+str(self.bill_details[0][1])+"\n")
        self.txtarea.insert(END, "\n=========================================================================")
        self.txtarea.insert(END, "\n S.N\tParticular\t\t\t\t\tQty\tRate\tTotal")
        self.txtarea.insert(END, "\n=========================================================================")
        s_n = 1
        for row in self.bill_details:
            total = float(row[3]) * float(row[4])
            grand_total += total
            self.txtarea.insert(END, "\n "+str(s_n)+'\t'+str(row[2])+"\t\t\t\t\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(total))
            s_n += 1
        self.txtarea.insert(END, "\n-------------------------------------------------------------------------")
        self.txtarea.insert(END, "\n Sign By: \t\t\t\t\t\t\t Total: "+str(grand_total))
        self.txtarea.insert(END, "\n=========================================================================")

    def get_bill_details(self):
        print(self.invoice_number)
        results = self.__query.execute(
            "SELECT b.phone_number, b.date_time, bd.particular, bd.qty, bd.rate, c.name, c.address FROM bills as b INNER JOIN customer as c on b.phone_number = c.phone_number INNER JOIN bill_details AS bd on b.invoice_number = bd.invoice_number where b.invoice_number = %s",
            self.invoice_number
        )
        print(results)
        if results > 0:
            self.bill_details = self.__query.fetchall()


#
# Bill_Generate(4)
# mainloop()
