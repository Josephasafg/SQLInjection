import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector.cursor_cext import CMySQLCursor


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='accounts',
                                                      user='root',
                                                      password='Gard2325',
                                                      port=3306)
            self.cursor: MySQLCursorPrepared = None
            self.prepared: MySQLCursorPrepared = None
            self.statement = """SELECT * FROM login where user=%s and password=%s"""
            self.verify_connection()

        except Error as e:
            print(e)

    def verify_connection(self):
        if self.connection.is_connected():
            db_info = self.connection.get_server_info()
            print(f"Connected to MySQL Server version {db_info}")

            self.cursor = self.connection.cursor()
            # self.cursor = self.connection.cursor(prepared=True)  # This creates a MySQLCursorPrepared object
            self.cursor.execute('select database();')
            record = self.cursor.fetchone()
            print(f'Your connection to database: {record}')
            self.cursor.close()

    def query(self, username, password):
        self.cursor = self.connection.cursor(prepared=True)
        # self.cursor.execute(f'SELECT * FROM login where user=\'{username}\' AND password=\'{password}\'')
        self.cursor.execute(self.statement, (username, password))

        result = self.cursor.fetchall()

        print(result)
        # if result[0] == username and result[1] == password:
        #     print(f"Correct input {result}")
        # else:
        #     raise ValueError('Failed to find entries in Database')
