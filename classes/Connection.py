import pymysql


class Connector:
    def __init__(self):
        try:
            self.my_connection = pymysql.connect(
                host='localhost', user='root', password='', port=3306, database='department'
            )
            self.my_cursor = self.my_connection.cursor()
        except Exception as e:
            print(e)