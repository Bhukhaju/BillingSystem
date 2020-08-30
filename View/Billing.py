from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes.Billing import Billings
from View.ListBill import ListBillView
from View.Generate import Bill_Generate


class BillingView:
    def __init__(self):
        # Create window object
        self.window = Tk()
        self.window.title('Billing System')
        self.window.geometry('900x600')
        self.show_menu()

        self.s_n = 1
        self.item_index = ''
        self.selected_item_data = ''
        self.s_n_update = ''


        self.customer_frame = Frame(self.window, bd=1, relief=RIDGE)
        self.customer_frame.place(x=15, y=30, width=650, height=100)

        # Customer detail
        self.customer = Label(self.window, text='Customer Detail', font=('bold', 14))
        self.customer.place(x=30, y=15)

        # Name
        self.name = StringVar()
        self.name_label = Label(self.customer_frame, text='Name', font=('bold', 12))
        self.name_label.place(x=15, y=30)
        self.name_entry = Entry(self.customer_frame, font=('bold', 12), textvariable = self.name)
        self.name_entry.place(x=15, y=55)

        # Address
        self.address = StringVar()
        self.address_label = Label(self.customer_frame, text='Address', font=('bold', 12))
        self.address_label.place(x=230,y=30)
        self.address_entry = Entry(self.customer_frame, font=('bold', 12), textvariable=self.address)
        self.address_entry.place(x=230, y=55)

        # Contact
        self.contact = StringVar()
        self.contact_label = Label(self.customer_frame, text='Phone Number', font=('bold', 12))
        self.contact_label.place(x=450, y=30)
        self.contact_entry = Entry(self.customer_frame, font=('bold', 12), textvariable=self.contact)
        self.contact_entry.place(x=450, y=55)

        '''Add Particular details'''
        # Particular frames
        self.particular_frame = Frame(self.window, bd=1, relief=RIDGE)
        self.particular_frame.place(x=15, y=160, width=220, height=290)

        # Particular detail
        self.particular_label = Label(self.window, text='Add Particular', font=('bold', 14))
        self.particular_label.place(x=30, y=145)

        # Particular
        self.particular = StringVar()
        self.particular_name = Label(self.particular_frame, text='Particular', font=('bold', 12))
        self.particular_name.place(x=15, y=30)
        self.particular_entry = Entry(self.particular_frame, font=('bold', 12), textvariable=self.particular)
        self.particular_entry.place(x=15, y=55)

        # Quantity
        self.qty = StringVar()
        self.qty = Label(self.particular_frame, text='Quantity', font=('bold', 12))
        self.qty.place(x=15, y=85)
        self.qty_entry = Entry(self.particular_frame, font=('bold', 12), textvariable=self.qty)
        self.qty_entry.place(x=15, y=110)

        # Rate
        self.rate = StringVar()
        self.rate = Label(self.particular_frame, text='Rate', font=('bold', 12))
        self.rate.place(x=15, y=140)
        self.rate_entry = Entry(self.particular_frame, font=('bold', 12), textvariable=self.rate)
        self.rate_entry.place(x=15, y=165)

        # Add Button
        self.add_btn = Button(self.particular_frame, text='Add', font=('regular', 12), width=8, command=self.insert)
        self.add_btn.place(x=15, y=195)

        # Update Button
        self.update_btn = Button(self.particular_frame, text='Update', font=('bold', 12), width=8, command=self.update_item)
        self.update_btn.place(x=118, y=195)

        # Delete Button
        self.delete_btn = Button(self.particular_frame, text='Delete', font=('bold', 12), width=8, bg='red', fg='white', command=self.delete_item)
        self.delete_btn.place(x=15, y=240)

        '''Tree View'''
        # Frame
        self.bill_detail = Frame(self.window, bd=1, relief=RIDGE)
        self.bill_detail.place(x=250, y=160, width=630, height=415)

        # Title
        self.bill_label = Label(self.window, text='Bill details', font=('bold', 14))
        self.bill_label.place(x=265, y=145)

        # Scroll
        self.scroll_x = Scrollbar(self.bill_detail, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.bill_detail, orient=VERTICAL)
        self.item_tree = ttk.Treeview(self.bill_detail, xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set, columns=('sn', 'name', 'qty', 'rate', 'total'), height=17)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.item_tree.xview)
        self.scroll_y.config(command=self.item_tree.yview)

        self.item_tree.place(x=15, y=30)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('sn', width=50)
        self.item_tree.column('name', width=250)
        self.item_tree.column('qty', width=50)
        self.item_tree.column('rate', width=120)
        self.item_tree.column('total', width=120)
        self.item_tree.heading('sn', text="S.N")
        self.item_tree.heading('name', text="PARTICULAR")
        self.item_tree.heading('qty', text="QTY")
        self.item_tree.heading('rate', text="RATE")
        self.item_tree.heading('total', text="TOTAL")

        # Print bill button
        self.print_btn = Button(self.window, text='PRINT', font=('Bold', 14), width=10, height=2, bg='blue', fg='white', command=self.print_bill)
        self.print_btn.place(x=70, y=475)

    # show menu bar
    def show_menu(self):
        top = self.window
        menu_bar = Menu(top)
        
        bill = Menu(menu_bar, tearoff=0)
        bill.add_command(label="List bills", command=self.list_bill)
        bill.add_separator()
        bill.add_command(label="Exit", command=top.quit)
        menu_bar.add_cascade(label="Bills", menu=bill)
        top.config(menu=menu_bar)

    def list_bill(self):
        ListBillView()

    def insert(self):
        try:
            if self.particular_entry.get() == '' or self.qty_entry.get() == '' or self.rate_entry.get() == '':
                messagebox.showwarning('Warning', 'Particular field(s) are empty')
            else:
                total = float(self.qty_entry.get()) * float(self.rate_entry.get())
                self.item_tree.insert('', 'end', text=('S.N', 'PARTICULAR', 'QTY', 'RATE', 'TOTAL'), values=(self.s_n, self.particular_entry.get(), self.qty_entry.get(), self.rate_entry.get(), total))
                self.item_tree.bind("<ButtonRelease-1>", self.select_item)
                self.clear_particular()
                self.s_n += 1
        except Exception as e:
            messagebox.showerror('Error', 'Quantity and Rate field should decimal or integer')

    def update_item(self):
        try:
            if self.particular_entry.get() == '' or self.qty_entry.get() == '' or self.rate_entry.get() == '':
                messagebox.showwarning('Warning', 'Particular field(s) are empty')
            else:
                particular = self.particular_entry.get()
                qty = self.qty_entry.get()
                rate = self.rate_entry.get()
                total = float(qty) * float(rate)
                focused = self.item_tree.focus()
                self.item_tree.insert("", str(focused)[1:], text=('S.N', 'PARTICULAR', 'QTY', 'RATE', 'TOTAL'), values=(self.s_n_update, str(particular), str(qty), str(rate), str(total)))
                self.item_tree.delete(focused)
                self.clear_particular()
        except Exception as e:
            messagebox.showerror('Error', 'Something is wrong please try again or contact admin')

    def delete_item(self):
        focused = self.item_tree.focus()
        self.item_tree.delete(focused)
        self.clear_particular()

    def print_bill(self):
        if self.contact_entry.get() == '' or len(self.item_tree.get_children()) <= 0:
            messagebox.showwarning('Warning', 'Customer details and Bill details required')
        else:
            rows = self.item_tree.get_children()
            billing = Billings()
            billing.print_bill(self.name_entry.get(), self.address_entry.get(), self.contact_entry.get(), self.item_tree)
            billing.insert()

    def select_item(self, event):
        selected_item = self.item_tree.selection()[0]
        # self.item_index = self.item_tree.item(selected_item, 'text')
        # print(self.item_index)
        self.selected_item_data = self.item_tree.item(selected_item, 'values')
        self.s_n_update = self.selected_item_data[0]
        self.clear_particular()
        self.particular_entry.insert(0, self.selected_item_data[1])
        self.qty_entry.insert(0, self.selected_item_data[2])
        self.rate_entry.insert(0, self.selected_item_data[3])

    def clear_particular(self):
        self.qty_entry.delete(0, END)
        self.particular_entry.delete(0, END)
        self.rate_entry.delete(0, END)


