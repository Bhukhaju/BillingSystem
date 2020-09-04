"""Import connector file, tkinter and billing file"""
from classes.Connection import Connector
from tkinter import messagebox
from View.Billing import BillingView


'''Create Class '''
class Login:
    def __init__(self):
        self.db = Connector()
        self.__query = self.db.my_cursor
        self.__window = ''
        self.__username = 'username'
        self.__password = 'password'

    '''Function for execute query'''
    def login_test(self, username, password):
        if self.__username == '' or self.__password == '':
            return False
        else:
            result = self.__query.execute('select * from users where username = %s and password = %s', (username, password))
            if result > 0:
                return True
            else:
                return False

    '''Function for login verify'''
    def login_verify(self, window, username, password):

        self.__window = window
        self.__username = username.get()
        self.__password = password.get()
        if self.login_test(self.__username, self.__password):
            self.__window.destroy()
            BillingView()
        else:
            messagebox.showerror('Error', ' Invalid Username or Password')
