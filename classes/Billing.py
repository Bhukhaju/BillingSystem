from classes.Connection import Connector
from datetime import datetime
from View.Generate import Bill_Generate


class Billings:
    def __init__(self):
        self.db = Connector()
        self.__query = self.db.my_cursor
        self.__item_tree = ''
        self.__name = ''
        self.__address = ''
        self.__phone_number = ''
        self.__bill_details = ''

    def print_bill(self, name, address, phone_number, item_tree):
        self.__item_tree = item_tree
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__bill_details = self.__item_tree.get_children()
        # for row in self.__bill_details:
        #     print(self.__item_tree.item(row)['values'])

    def insert(self):
        current_date_time = datetime.now()
        customer_result = self.__query.execute(
            'select * from customer where phone_number = %s',
            self.__phone_number)
        if customer_result == 0:
            self.__query.execute(
                'insert into customer (phone_number, address, name) values(%s, %s, %s)',
                (self.__phone_number, self.__address, self.__name)
            )

        self.__query.execute(
            'insert into bills ( phone_number,date_time) values(%s, %s)',
            (self.__phone_number, current_date_time)
        )
        invoice_id = self.__query.lastrowid
        for row in self.__bill_details:
            values = self.__item_tree.item(row)['values']
            print(values)
            self.__query.execute(
                'insert into bill_details (invoice_number, particular, qty, rate) values(%s, %s, %s, %s)',
                (invoice_id, values[1], values[2], values[3])
            )
        self.db.my_connection.commit()
        self.db.my_connection.close()
        Bill_Generate(invoice_id)
