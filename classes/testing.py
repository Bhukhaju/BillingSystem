import unittest
from classes.Login import *
# from classes.Item import *
class MyTest(unittest.TestCase):
    # def test_add(self):
    #     op = Operation()
    #     actual_result = op.add(5, 6)
    #     expected_result = 11
    #     self.assertEqual(expected_result, actual_result)
    # def test_multiply(self):
    #     op = Operation()
    #     actual_result = op.multiply(5, 6)
    #     expected_result = 30
    #     self.assertEqual(expected_result, actual_result)
    # def test_check_even(self):
    #     op = Operation()
    #     actual_result = op.check_even(5)
    #     # expected_result = False
    #     # self.assertEqual(expected_result, actual_result)
    #     self.assertFalse(actual_result)
    def test_login(self):
        login = Login()
        actual_result = login.login_test('a','a')
        self.assertTrue(actual_result)
