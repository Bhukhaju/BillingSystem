from classes.Connection import Connector
from tkinter import messagebox
from View.Billing import BillingView


class Login:
    def __init__(self):
        self.db = Connector()
        self.__query = self.db.my_cursor
        self.__window = ''
        self.__username = 'username'
        self.__password = 'password'

    def login_test(self, username, password):

        if self.__username == '' or self.__password == '':
            return False
        else:
            result = self.__query.execute('select * from users where username = %s and password = %s', (username, password))
            if result > 0:
                return True
            else:
                return False

    def login_verify(self, window, username, password):

        self.__window = window
        self.__username = username.get()
        self.__password = password.get()
        if self.login_test(self.__username, self.__password):
            self.__window.destroy()
            BillingView()
        else:
            messagebox.showerror('Error', ' Invalid Username or Password')

        # if self.__username == '' or self.__password == '':
        #     # messagebox.showwarning('Error', 'Username and Password required')
        #     return False
        # else:
        #     result = self.__query.execute('select * from users where username = %s and password = %s', (username, password))
        #     # print(result)
        #     if result > 0:
        #         # self.__window.destroy()
        #         # BillingView()
        #         return True
        #     else:
        #         # messagebox.showerror('Error', ' Invalid Username or Password')
        #         return False




"""
Documentation
Class name: Login
Public method : login_verify(window, username, password)
eg
login=Login()
login.login_verify(window, username, password)
"""