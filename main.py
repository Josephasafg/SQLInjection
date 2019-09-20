from tkinter import *

from login_page import LoginPage


class Login(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        width = self.winfo_screenwidth() // 4
        height = self.winfo_screenheight() // 4
        self.container = Frame(self, width=width, height=height)
        self.container.grid_propagate(False)
        self.container.pack(side=TOP, fill=BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = dict()

        frame = LoginPage(self.container, self)
        self.frames[LoginPage] = frame
        frame.grid(row=0, column=0, sticky=NSEW)
        self.show_frames(LoginPage)

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()


if __name__ == '__main__':
    app = Login()
    app.mainloop()
