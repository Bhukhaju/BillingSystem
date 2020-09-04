"""Import tkinter and Register file"""
from tkinter import *
from classes.Register import Register

"""Create class"""
class RegisterView:
    def __init__(self):

        """Create window object"""
        self.window = Tk()
        self.window.title('Register')
        self.window.geometry('450x400')

        """Register Part"""
        """Username for Register"""
        self.username = StringVar()
        self.username_label = Label(self.window, text='Username', font=('bold', 14))
        self.username_label.grid(row=0, column=0, sticky=W, pady=10, padx=50)
        self.username_entry = Entry(self.window, textvariable=self.username, width=30)
        self.username_entry.grid(row=0, column=1, sticky=W)

        """Password for register"""
        self.password = StringVar()
        self.password_label = Label(self.window, text='Password', font=('bold', 14))
        self.password_label.grid(row=1, column=0, sticky=W, pady=10, padx=50)
        self.password_entry = Entry(self.window, textvariable=self.password, width=30, show='*')
        self.password_entry.grid(row=1, column=1, sticky=W)

        """Full name for register """
        self.fullname = StringVar()
        self.fullname_label = Label(self.window, text='Full Name', font=('bold', 14))
        self.fullname_label.grid(row=2, column=0, sticky=W, pady=10, padx=50)
        self.fullname_entry = Entry(self.window, textvariable=self.fullname, width=30)
        self.fullname_entry.grid(row=2, column=1, sticky=W)

        """Address for register"""
        self.address = StringVar()
        self.address_label = Label(self.window, text='Address', font=('bold', 14))
        self.address_label.grid(row=3, column=0, sticky=W, pady=10, padx=50)
        self.address_entry = Entry(self.window, textvariable=self.address, width=30)
        self.address_entry.grid(row=3, column=1, sticky=W)

        """Phone Number for register"""
        self.phone = StringVar()
        self.phone_label = Label(self.window, text='Phone', font=('bold', 14))
        self.phone_label.grid(row=4, column=0, sticky=W, pady=10, padx=50)
        self.phone_entry = Entry(self.window, textvariable=self.phone, width=30)
        self.phone_entry.grid(row=4, column=1, sticky=W)

        """Email for register"""
        self.email = StringVar()
        self.email_label = Label(self.window, text='Email', font=('bold', 14))
        self.email_label.grid(row=5, column=0, sticky=W, pady=10, padx=50)
        self.email_entry = Entry(self.window, textvariable=self.email, width=30)
        self.email_entry.grid(row=5, column=1, sticky=W)

        """Submit button"""
        self.submit_btn = Button(self.window, text='Submit', font=('bold', 14), command=self.register_user)
        self.submit_btn.grid(row=6, column=1, pady=30)

        """Reset Button"""
        self.reset_btn = Button(self.window, text='Reset', font=('bold', 12), command=self.clear_particular)
        self.reset_btn.grid(row=6, column=0, pady=30)

        """Function for pass entry value to classes.Register import Register"""
    def register_user(self):
        register = Register()
        register.register_user(self.username_entry.get(), self.password_entry.get(), self.fullname_entry.get(),
                               self.address_entry.get(), self.phone_entry.get(), self.email_entry.get())

    def clear_particular(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.fullname_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)