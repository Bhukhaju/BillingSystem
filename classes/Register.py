"""Import connector file and tkinter"""
from classes.Connection import Connector
from tkinter import messagebox


"""Create Class"""
class Register:
    def __init__(self):
        self.db = Connector()
        self.__query = self.db.my_cursor
        self.__window = ''
        self.__username = ''
        self.__password = ''
        self.__fullname = ''
        self.__address = ''
        self.__phone = ''
        self.__email = ''

    """Function for Register of Employee"""
    def register_user(self, username, password, fullname, address, phone, email):
        self.__username = username
        self.__password = password
        self.__fullname = fullname
        self.__address = address
        self.__phone = phone
        self.__email = email
        if self.__username == '' or self.__password == '' or self.__fullname == '' or self.__address == '' or self.__phone == '' or self.__email == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            result_username = self.__query.execute('select * from users where username = %s', self.__username)
            result_phone = self.__query.execute('select * from users where phone = %s', self.__phone)
            result_email = self.__query.execute('select * from users where email = %s', self.__email)
            if result_username > 0:
                messagebox.showwarning('Error', 'Username already exists')
            elif result_phone > 0:
                messagebox.showwarning('Error', 'Phone number already exists')
            elif result_email > 0:
                messagebox.showwarning('Error', 'Email already exists')
            else:
                try:
                    if self.insert(self.__username, self.__password, self.__fullname, self.__address, self.__phone, self.__email):
                        messagebox.showinfo('Success', 'Register Successfully')
                    else:
                        messagebox.showerror('Error', 'Something is wrong please try again or contact admin')
                except Exception as e:
                    messagebox.showerror('Error', 'Something is wrong please try again or contact admin')
        self.db.my_connection.close()


    """Function for insert into database"""
    def insert(self, username, password, fullname, address, phone, email):
        result = self.__query.execute(
            'INSERT INTO users ( username, password, name, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
            (username, password, fullname, address, phone, email))
        if result > 0:
            self.db.my_connection.commit()
            return True
        else:
            return False

