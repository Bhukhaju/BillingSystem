from tkinter import *
from classes.Register import Register


class RegisterView:
    def __init__(self):
        # Create window object
        self.window = Tk()

        self.window.title('Register')
        self.window.geometry('450x400')

        # Username
        self.username = StringVar()
        self.username_label = Label(self.window, text='Username', font=('bold', 14))
        self.username_label.grid(row=0, column=0, sticky=W, pady=10, padx=50)
        self.username_entry = Entry(self.window, textvariable=self.username, width=30)
        self.username_entry.grid(row=0, column=1, sticky=W)

        # Password
        self.password = StringVar()
        self.password_label = Label(self.window, text='Password', font=('bold', 14))
        self.password_label.grid(row=1, column=0, sticky=W, pady=10, padx=50)
        self.password_entry = Entry(self.window, textvariable=self.password, width=30, show='*')
        self.password_entry.grid(row=1, column=1, sticky=W)

        # Fullname
        self.fullname = StringVar()
        self.fullname_label = Label(self.window, text='Full Name', font=('bold', 14))
        self.fullname_label.grid(row=2, column=0, sticky=W, pady=10, padx=50)
        self.fullname_entry = Entry(self.window, textvariable=self.fullname, width=30)
        self.fullname_entry.grid(row=2, column=1, sticky=W)

        # Address
        self.address = StringVar()
        self.address_label = Label(self.window, text='Address', font=('bold', 14))
        self.address_label.grid(row=3, column=0, sticky=W, pady=10, padx=50)
        self.address_entry = Entry(self.window, textvariable=self.address, width=30)
        self.address_entry.grid(row=3, column=1, sticky=W)

        # Phone
        self.phone = StringVar()
        self.phone_label = Label(self.window, text='Phone', font=('bold', 14))
        self.phone_label.grid(row=4, column=0, sticky=W, pady=10, padx=50)
        self.phone_entry = Entry(self.window, textvariable=self.phone, width=30)
        self.phone_entry.grid(row=4, column=1, sticky=W)

        # Email
        self.email = StringVar()
        self.email_label = Label(self.window, text='Email', font=('bold', 14))
        self.email_label.grid(row=5, column=0, sticky=W, pady=10, padx=50)
        self.email_entry = Entry(self.window, textvariable=self.email, width=30)
        self.email_entry.grid(row=5, column=1, sticky=W)

        # Submit Button
        self.submit_btn = Button(self.window, text='Submit', font=('bold', 14), command=self.register_user)
        self.submit_btn.grid(row=6, column=1, pady=30)

        # Reset Button
        self.reset_btn = Button(self.window, text='Reset', font=('bold', 12))
        self.reset_btn.grid(row=6, column=0, pady=30)

    def register_user(self):
        register = Register()
        register.register_user(self.username_entry, self.password_entry, self.fullname_entry, self.address_entry, self.phone_entry, self.email_entry)

