from tkinter import *
from tkinter import ttk
from classes.Connection import Connector
from tkinter import messagebox
from View.Generate import Bill_Generate

class ListBillView:
    def __init__(self):
        self.db = Connector()
        self.__query = self.db.my_cursor
        self.window = Tk()
        self.window.title('Search Bills')
        self.window.geometry('1135x600')

        self.bill_number_entry = ''
        self.phone_number_entry = ''

        self.selected_item_data = ''

        self.bill_item_tree = ''
        self.bill_details_item_tree = ''

        self.search_bill()
        self.bill_lists()
        self.bill_details()

    def search_bill(self):
        # Frame
        search_frame = Frame(self.window, bd=1, relief=RIDGE)
        search_frame.place(x=15, y=30, width=550, height=100)

        # Label
        search_label = Label(self.window, text='Search', font=('bold', 14))
        search_label.place(x=30, y=15)

        # Bill Number
        # self.bill_number = StringVar()
        bill_number_label = Label(search_frame, text='Bill Number', font=('bold', 12))
        bill_number_label.place(x=15, y=30)
        self.bill_number_entry = Entry(search_frame, font=('bold', 12))
        self.bill_number_entry.place(x=15, y=55)

        # Phone Number
        # self.phone_number = StringVar()
        phone_number_label = Label(search_frame, text='Phone Number', font=('bold', 12))
        phone_number_label.place(x=230, y=30)
        self.phone_number_entry = Entry(search_frame, font=('bold', 12))
        self.phone_number_entry.place(x=230, y=55)

        # Search Button
        search_btn = Button(search_frame, text='Search', font=('regular', 12), width=8, height=2, command=self.search)
        search_btn.place(x=450, y=30)

    def bill_lists(self):
        # Frame
        bill_detail = Frame(self.window, bd=1, relief=RIDGE)
        bill_detail.place(x=15, y=160, width=460, height=415)

        # Title
        bill_label = Label(self.window, text='Bill lists', font=('bold', 14))
        bill_label.place(x=30, y=145)

        # Scroll
        scroll_x = Scrollbar(bill_detail, orient=HORIZONTAL)
        scroll_y = Scrollbar(bill_detail, orient=VERTICAL)
        self.bill_item_tree = ttk.Treeview(bill_detail, xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set, columns=('bill_number', 'name', 'phone_number'),
                                      height=17)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.bill_item_tree.xview)
        scroll_y.config(command=self.bill_item_tree.yview)

        self.bill_item_tree.place(x=15, y=30)
        self.bill_item_tree['show'] = 'headings'
        self.bill_item_tree.column('bill_number', width=100)
        self.bill_item_tree.column('name', width=200)
        self.bill_item_tree.column('phone_number', width=120)
        self.bill_item_tree.heading('bill_number', text="BILL NUMBER")
        self.bill_item_tree.heading('name', text="NAME")
        self.bill_item_tree.heading('phone_number', text="PHONE NUMBER")

        self.__query.execute('SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN customer as c on b.phone_number = c.phone_number')
        rows = self.__query.fetchall()
        for row in rows:
            self.bill_item_tree.insert('', 'end', text=('BILL NUMBER', 'NAME', 'PHONE NUMBER'), values=row)
            self.bill_item_tree.bind("<ButtonRelease-1>", self.select_item)

        # self.__query.execute('')

    def bill_details(self):
        # Frame
        bill_detail = Frame(self.window, bd=1, relief=RIDGE)
        bill_detail.place(x=490, y=160, width=630, height=415)

        # Title
        bill_label = Label(self.window, text='Bill details', font=('bold', 14))
        bill_label.place(x=505, y=145)

        # Scroll
        scroll_x = Scrollbar(bill_detail, orient=HORIZONTAL)
        scroll_y = Scrollbar(bill_detail, orient=VERTICAL)
        self.bill_details_item_tree = ttk.Treeview(bill_detail, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, columns=('sn', 'name', 'qty', 'rate', 'total'),
                                      height=17)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.bill_details_item_tree.xview)
        scroll_y.config(command=self.bill_details_item_tree.yview)

        self.bill_details_item_tree.place(x=15, y=30)
        self.bill_details_item_tree['show'] = 'headings'
        self.bill_details_item_tree.column('sn', width=50)
        self.bill_details_item_tree.column('name', width=250)
        self.bill_details_item_tree.column('qty', width=50)
        self.bill_details_item_tree.column('rate', width=120)
        self.bill_details_item_tree.column('total', width=120)
        self.bill_details_item_tree.heading('sn', text="S.N")
        self.bill_details_item_tree.heading('name', text="PARTICULAR")
        self.bill_details_item_tree.heading('qty', text="QTY")
        self.bill_details_item_tree.heading('rate', text="RATE")
        self.bill_details_item_tree.heading('total', text="TOTAL")

        # Print bill button
        print_btn = Button(self.window, text='PRINT', font=('Bold', 14), width=10, height=2, bg='blue', fg='white', command=self.print_current_bill)
        print_btn.place(x=800, y=45)

    def search(self):
        if self.bill_number_entry.get() == '' and self.phone_number_entry.get() == '':
            results = self.__query.execute(
                'SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN customer as c on b.phone_number = c.phone_number'
            )
        else:
            results = self.__query.execute(
                'SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN customer as c on b.phone_number = c.phone_number where b.invoice_number = %s or b.phone_number = %s',
                (self.bill_number_entry.get(), self.phone_number_entry.get())
            )
        self.bill_item_tree.delete(*self.bill_item_tree.get_children())
        self.bill_details_item_tree.delete(*self.bill_details_item_tree.get_children())
        if results > 0:
            rows = self.__query.fetchall()
            for row in rows:
                self.bill_item_tree.insert('', 'end', text=('BILL NUMBER', 'NAME', 'PHONE NUMBER'), values=row)
                self.bill_item_tree.bind("<ButtonRelease-1>", self.select_item)
        else:
            messagebox.showwarning('Warning', 'Bills not found')

    def select_item(self, event):
        selected_item = self.bill_item_tree.selection()[0]
        # self.item_index = self.item_tree.item(selected_item, 'text')
        # print(self.item_index)
        self.selected_item_data = self.bill_item_tree.item(selected_item, 'values')
        print(self.selected_item_data)
        self.list_bill_details()

    def list_bill_details(self):
        results = self.__query.execute(
            'Select * from bill_details where invoice_number = %s', self.selected_item_data[0]
        )
        self.bill_details_item_tree.delete(*self.bill_details_item_tree.get_children())
        if results > 0:
            s_n = 1
            rows = self.__query.fetchall()
            for row in rows:
                print(row)
                total = float(row[3]) * float(row[4])
                self.bill_details_item_tree.insert('', 'end', text=('S.N', 'PARTICULAR', 'QTY', 'RATE', 'TOTAL'), values=(s_n, row[2], row[3], row[4], total))
                s_n += 1

    def print_current_bill(self):
        Bill_Generate(self.selected_item_data[0])
#
# ListBillView()
# mainloop()
