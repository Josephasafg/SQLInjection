import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='accounts',
                                                      user='root',
                                                      password='Gard2325',
                                                      port=3306)
            self.cursor = None
            self.verify_connection()

        except Error as e:
            print(e)

    def verify_connection(self):
        if self.connection.is_connected():
            db_info = self.connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")

            self.cursor = self.connection.cursor()
            self.cursor.execute('select database();')
            record = self.cursor.fetchone()
            print(f'Your connection to database: {record}')

    def query(self, username, password):
        # self.cursor.execute(f'SELECT * FROM login where user=\'{username}\'')
        self.cursor.execute('SELECT * FROM login where user=\'\' or 1=\'1\' ')
        print(self.cursor.fetchall())