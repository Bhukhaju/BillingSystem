"""Import testing"""
import unittest

"""Import python file"""
from View.ListBill import ListBillView
from classes.Login import *
from classes.Register import Register


"""Create Class for testing """
class MyTest(unittest.TestCase):
    """Function of login verify testing"""
    def test_login(self):
        login = Login()
        actual_result = login.login_test('a', 'a')
        self.assertTrue(actual_result)

    def test_login1(self):
        login = Login()
        actual_result = login.login_test('a', 'v')
        self.assertFalse(actual_result)

    """Function of register verify testing"""
    def test_register(self):
        r = Register()
        actual_result = r.insert("z", "z", "z", "z", "1", "e")
        self.assertTrue(actual_result)

    """Function of list view testing"""
    def ListBillView(self):
        l = ListBillView()
        actual_result = l.list_bill_details()
        self.assertTrue(actual_result)

    """function of search testing"""
    def search(self):
        s = ListBillView()
        actual_result = s.search()
        self.assertTrue(actual_result)

