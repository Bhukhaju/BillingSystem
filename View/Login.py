from tkinter import *
from classes.Login import Login
from View.Register import RegisterView


class LoginView:
    def __init__(self):
        # Create window object
        self.window = Tk()

        self.window.title('User Login')
        self.window.geometry('300x300')

        # Login Parts
        # Username
        self.username = StringVar()
        self.username_label = Label(self.window, text='Username', font=('bold', 14))
        self.username_label.grid(row=0, column=0, sticky=W, pady=10, padx=50)
        self.username_entry = Entry(self.window, textvariable=self.username, width=15, font=('regular', 16))
        self.username_entry.grid(row=1, column=0, sticky=W, padx=50)

        # Password
        self.password = StringVar()
        self.password_label = Label(self.window, text='Password', font=('bold', 14))
        self.password_label.grid(row=2, column=0, sticky=W, pady=10, padx=50)
        self.password_entry = Entry(self.window, textvariable=self.password, width=15, show='*', font=('regular', 16))
        self.password_entry.grid(row=3, column=0, sticky=W, padx=50)

        # Login Button
        self.login_btn = Button(self.window, text='Login', font=('bold', 14), command=self.login_verify)

        self.login_btn.grid(row=4, column=0, pady=20)

        # Register Button
        self.register_btn = Button(self.window, text='Register', font=('bold', 12), command=self.register_view)
        self.register_btn.grid(row=5, column=0)

        # Start program
        self.window.mainloop()

    def login_verify(self):
        login = Login()
        login.login_verify(self.window, self.username_entry, self.password_entry)

    def register_view(self):
        RegisterView()
        self.window.destroy()

