from tkinter import *
from tkinter import ttk

import mysql

from DatabaseConnector import DatabaseConnection

MEDIUM_FONT = ("verdana", 14)


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='black')
        self.user_name = StringVar()
        self.password = StringVar()
        self.user_name_entry = Entry(self, textvariable=self.user_name,
                                     font=MEDIUM_FONT)
        self.password_entry = Entry(self, textvariable=self.password,
                                    font=MEDIUM_FONT, show='*')
        self.enter_button = ttk.Button(self, text="Enter",
                                       command=self.authentication)
        self.exit_button = ttk.Button(self, text="Exit",
                                      command=self.quit)
        self.login_window()

    def create_sub_frame(self, row, col, r_span, c_span, border_color="red") -> Frame:
        frame = Frame(self, highlightbackground=border_color, highlightcolor=border_color,
                      highlightthickness=2, bg='black')
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.grid(row=row, column=col, rowspan=r_span, columnspan=c_span, sticky=W + E + N + S)
        return frame

    def login_window(self):
        user_label = Label(self, text='User Name:',
                           font=MEDIUM_FONT,
                           fg='white',
                           bg='black')

        password_label = Label(self, text='Password:',
                               font=MEDIUM_FONT,
                               fg='white',
                               bg='black')

        user_label.pack()
        self.user_name_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        self.enter_button.pack()
        self.exit_button.pack()

    def authentication(self):
        try:
            db = DatabaseConnection()
            db.query(self.user_name.get(), self.password.get())
        except mysql.connector.Error as error:
            print(error)
        finally:
            if db.connection.is_connected():
                db.cursor.close()
                db.connection.close()

    def quit(self):
        exit(0)
