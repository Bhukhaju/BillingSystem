"""Import ttk, Connector file, messagenox and Generate file """
from tkinter import *
from tkinter import ttk
from classes.Connection import Connector
from tkinter import messagebox
from View.Generate import Bill_Generate


"""Create class"""
class ListBillView:
    def __init__(self):
        """Create connector object"""
        self.db = Connector()
        self.__query = self.db.my_cursor
        """Create windows object"""
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

    """Function search bill"""
    def search_bill(self):

        """Create search frame"""
        search_frame = Frame(self.window, bd=1, relief=RIDGE)
        search_frame.place(x=15, y=30, width=550, height=100)

        """label for search"""
        search_label = Label(self.window, text='Search', font=('bold', 14))
        search_label.place(x=30, y=15)

        """Searching bill number parts"""
        bill_number_label = Label(search_frame, text='Bill Number', font=('bold', 12))
        bill_number_label.place(x=15, y=30)
        self.bill_number_entry = Entry(search_frame, font=('bold', 12))
        self.bill_number_entry.place(x=15, y=55)

        """Searching phone number parts"""
        phone_number_label = Label(search_frame, text='Phone Number', font=('bold', 12))
        phone_number_label.place(x=230, y=30)
        self.phone_number_entry = Entry(search_frame, font=('bold', 12))
        self.phone_number_entry.place(x=230, y=55)

        """Button for search"""
        search_btn = Button(search_frame, text='Search', font=('regular', 12), width=8, height=2, command=self.search)
        search_btn.place(x=450, y=30)

    """Tree view for bill list"""
    """function for bill list"""
    def bill_lists(self):
        """"Frame for bill list"""
        bill_detail = Frame(self.window, bd=1, relief=RIDGE)
        bill_detail.place(x=15, y=160, width=460, height=415)

        """Label for bill list"""
        bill_label = Label(self.window, text='Bill lists', font=('bold', 14))
        bill_label.place(x=30, y=145)

        """Tree view part"""
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
        """Query for insert into tree view"""
        self.__query.execute('SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN'
                             ' customer as c on b.phone_number = c.phone_number')
        rows = self.__query.fetchall()
        for row in rows:
            self.bill_item_tree.insert('', 'end', text=('BILL NUMBER', 'NAME', 'PHONE NUMBER'), values=row)
            self.bill_item_tree.bind("<ButtonRelease-1>", self.select_item)

    """Tree view for bill details"""
    """Function for bill details"""
    def bill_details(self):
        """Frame for bill details"""
        bill_detail = Frame(self.window, bd=1, relief=RIDGE)
        bill_detail.place(x=490, y=160, width=630, height=415)

        """label for bill details"""
        bill_label = Label(self.window, text='Bill details', font=('bold', 14))
        bill_label.place(x=505, y=145)

        """Tree view part"""
        scroll_x = Scrollbar(bill_detail, orient=HORIZONTAL)
        scroll_y = Scrollbar(bill_detail, orient=VERTICAL)
        self.bill_details_item_tree = ttk.Treeview(bill_detail, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,
                                                   columns=('sn', 'name', 'qty', 'rate', 'total'),height=17)
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

        """button for print bill"""
        print_btn = Button(self.window, text='PRINT', font=('Bold', 14), width=10, height=2, bg='blue', fg='white',
                           command=self.print_current_bill)
        print_btn.place(x=800, y=45)

    """Function for Binary Search for bill"""
    def binary_search(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                return list[mid]
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    """function for search by query"""
    def searchby_id(self, id):
        results = self.__query.execute('SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN'
                                       ' customer as c on b.phone_number = c.phone_number')
        data=self.__query.fetchall()
        return self.binary_search(data, id)

    """Function for search for Number"""
    def search(self):
        if self.bill_number_entry.get() == '' and self.phone_number_entry.get() == '':
            self.__query.execute(
                'SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN customer as c on '
                'b.phone_number = c.phone_number'
            )
        elif self.bill_number_entry.get() != '':
            print(self.bill_number_entry.get())
            rows = self.searchby_id(int(self.bill_number_entry.get()))
            self.bill_item_tree.delete(*self.bill_item_tree.get_children())
            self.bill_details_item_tree.delete(*self.bill_details_item_tree.get_children())
            self.bill_item_tree.insert('', 'end', text=('BILL NUMBER', 'NAME', 'PHONE NUMBER'), values=rows)
        elif self.phone_number_entry.get() != '':
            self.__query.execute(
                'SELECT b.invoice_number, c.name, b.phone_number FROM bills as b INNER JOIN customer as c on '
                'b.phone_number = c.phone_number where b.phone_number = %s',
                (self.phone_number_entry.get(),)
            )
            rows = self.__query.fetchall()
            print(rows)
            self.bill_item_tree.delete(*self.bill_item_tree.get_children())
            self.bill_details_item_tree.delete(*self.bill_details_item_tree.get_children())
            if len(rows) > 0:
                for row in rows:
                    self.bill_item_tree.insert('', 'end', text=('BILL NUMBER', 'NAME', 'PHONE NUMBER'), values=row)
                    self.bill_item_tree.bind("<ButtonRelease-1>", self.select_item)
            else:
                messagebox.showwarning('Warning', 'Bills not found')

    """Function for select item in tree vew"""
    def select_item(self, event):
        selected_item = self.bill_item_tree.selection()[0]
        self.selected_item_data = self.bill_item_tree.item(selected_item, 'values')
        self.list_bill_details()

    """Function for show in bill detail"""
    def list_bill_details(self):
        results = self.__query.execute(
            'Select * from bill_details where invoice_number = %s', self.selected_item_data[0]
        )
        self.bill_details_item_tree.delete(*self.bill_details_item_tree.get_children())
        if results > 0:
            s_n = 1
            rows = self.__query.fetchall()
            for row in rows:
                total = float(row[3]) * float(row[4])
                self.bill_details_item_tree.insert('', 'end', text=('S.N', 'PARTICULAR', 'QTY', 'RATE', 'TOTAL'),
                                                   values=(s_n, row[2], row[3], row[4], total))
                s_n += 1
    """function for bill generate"""
    def print_current_bill(self):
        Bill_Generate(self.selected_item_data[0])

