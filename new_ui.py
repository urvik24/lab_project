import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self, width=500, height=500)
        container.pack(side="top", fill="both", expand=True)
        frameList = [LoginMain, Register, Page2]
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in frameList:
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Page2)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# second window frame page1
class LoginMain(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_0 = tk.Label(self, text="LOGIN CREDENTIALS", font=("Times New Roman", 20), fg='blue')
        self.label_id = tk.Label(self, text="Staff ID", width=20, font=("bold", 10))
        self.entry_id = tk.Entry(self)
        self.label_pass = tk.Label(self, text="Password", width=20, font=("bold", 10))
        self.entry_pass = tk.Entry(self, show="*")
        self.label_5 = tk.Label(self, text="New Account?", width=20, font=("bold", 10))
        self.b = tk.Button(self, text='Submit', width=20, bg='brown', fg='red', command=self.submit)
        self.b1 = tk.Button(self, text='Register', width=20, bg='brown', fg='red', command=lambda: controller.show_frame(Register))
        self.b2 = tk.Button(self, text='Back', width=10, bg='brown', fg='red', command=self.back)
        self.loginpage()

    def loginpage(self):
        self.label_0.grid(row=0, column=4, padx=10, pady=10)
        self.label_id.grid(row=1, column=4, padx=10, pady=10)
        self.entry_id.grid(row=2, column=4, padx=10, pady=10)
        self.label_pass.grid(row=3, column=4, padx=10, pady=10)
        self.entry_pass.grid(row=4, column=4, padx=10, pady=10)
        self.label_5.grid(row=5, column=4, padx=10, pady=10)
        self.b.grid(row=6, column=4, padx=10, pady=10)
        self.b1.grid(row=7, column=4, padx=10, pady=10)
        self.b2.grid(row=8, column=4, padx=10, pady=10)

    def submit(self):
        pass

    def back(self):
        pass


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.newloginpage()

    def newloginpage(self):
        self.label_1 = tk.Label(self, text="Login Details",width=20,font=("Times New Roman", 20))
        self.label_1.place(x=5,y=1)

        self.label_0 = tk.Label(self, text="Enter the details",width=20,font=("Arial", 15))
        self.label_0.place(x=100,y=60)

        self.label_id = tk.Label(self, text="Staff ID",width=20,font=("bold", 10))
        self.label_id.place(x=68,y=160)

        self.entry_id = tk.Entry(self)
        self.entry_id.place(x=240,y=160)

        self.label_pass = tk.Label(self, text="Password",width=20,font=("bold", 10))
        self.label_pass.place(x=68,y=200)
        self.entry_pass = tk.Entry(self,show="*")
        self.entry_pass.place(x=240,y=200)
        self.label_conpass = tk.Label(self, text="Confirm Password",width=20,font=("bold", 10))
        self.label_conpass.place(x=68,y=230)
        self.entry_conpass = tk.Entry(self,show="*")
        self.entry_conpass.place(x=240,y=230)

        self.b1= tk.Button(self, text='Submit',width=10,bg='brown',fg='white').place(x=195,y=275)
        self.b2= tk.Button(self, text='Back',width=10,bg='brown',fg='white').place(x=195,y=315)

    def newlogin(self):
        pass


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(LoginMain))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Driver Code
app = tkinterApp()
app.mainloop()
