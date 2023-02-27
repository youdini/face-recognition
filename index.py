
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydb")
cursor.execute("USE mydb")
db.commit()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FRAME0 = OUTPUT_PATH / \
    Path(r"./assets/frame0")
ASSETS_PATH_FRAME5 = OUTPUT_PATH / \
    Path(r"./assets/frame5")
ASSETS_PATH_FRAME2 = OUTPUT_PATH / \
    Path(r"./assets/frame2")


def frame0(path: str) -> Path:
    return ASSETS_PATH_FRAME0 / Path(path)


def frame2(path: str) -> Path:
    return ASSETS_PATH_FRAME2 / Path(path)


def frame5(path: str) -> Path:
    return ASSETS_PATH_FRAME5 / Path(path)


def checkLogin(uname, pword):
    if uname == "admin" or pword == "":
        return False
    else:
        return True


def checkRegister(uname, pword, conpword):
    if uname == "" or pword == "" or conpword == "":
        messagebox.showerror(
            title="Error", message="Don't forget to fill all the fields")
        return False
    else:
        if pword != conpword:
            messagebox.showerror(
                title="Error", message="Passwords don't match")
            return False
        else:
            return True

# mainwindow


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x832")
        self.master.title("Face Recognition Student Identifier")
        self.master.configure(bg="#fff")

        self.canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        # logo
        self.image_image_1 = PhotoImage(
            file=frame0("image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=self.image_image_1
        )

        # app name
        self.canvas.create_text(
            38.0,
            416.0,
            anchor="nw",
            text="Face Recognition Student Identifier",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 32 * -1)
        )

        # reactangle for signin
        self.canvas.create_rectangle(
            640.0,
            0.0,
            1280.0,
            832.0,
            fill="#FFFFFF",
            outline=""
        )

        # face recognition image
        self.image_image_2 = PhotoImage(
            file=frame0("image_2.png"))
        self.image_2 = self.canvas.create_image(
            960.0,
            230.0,
            image=self.image_image_2
        )

        # username input bg
        self.image_image_3 = PhotoImage(
            file=frame0("image_3.png"))
        self.image_3 = self.canvas.create_image(
            959.0,
            484.0,
            image=self.image_image_3
        )

        # password input bg
        self.image_image_4 = PhotoImage(
            file=frame0("image_4.png"))
        self.image_4 = self.canvas.create_image(
            959.0,
            587.0,
            image=self.image_image_4
        )

        # login button bg
        self.button_image_1 = PhotoImage(
            file=frame0("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.button_1.place(
            x=741.0,
            y=656.0,
            width=437.0,
            height=69.0
        )

        # username label
        self.canvas.create_text(
            774.0,
            423.0,
            anchor="nw",
            text="Username",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )
        # register label
        self.canvas.create_text(
            884.0,
            740.0,
            anchor="nw",
            text="Don’t have an account? ",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        # password label
        self.canvas.create_text(
            774.0,
            526.0,
            anchor="nw",
            text="Password",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        # username input bg
        self.entry_image_1 = PhotoImage(
            file=frame0("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            959.5,
            484.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman Regular", 18 * -1)
        )
        self.entry_1.place(
            x=779.0,
            y=463.0,
            width=361.0,
            height=41.0
        )

        # password input bg
        self.entry_image_2 = PhotoImage(
            file=frame0("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            959.5,
            586.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman Regular", 18 * -1),
            show="•"
        )
        self.entry_2.place(
            x=779.0,
            y=565.0,
            width=361.0,
            height=41.0
        )

        self.button_image_2 = PhotoImage(
            file=frame0("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.register,
            relief="flat"
        )
        self.button_2.place(
            x=872.0,
            y=774.0,
            width=175.0,
            height=35.0
        )

    def register(self):
        newWindow = Tk()
        newWindow.resizable(False, False)
        self.app = RegisterWindow(newWindow)
        newWindow.destroy()

    def login(self):
        uname = self.entry_1.get()
        pword = self.entry_2.get()
        c = checkLogin(uname, pword)
        if c == True:
            try:
                cursor.execute(
                    f"SELECT * FROM users WHERE username = '{uname}' AND password = '{pword}'")
                result = cursor.fetchone()
                if result:
                    messagebox.showinfo("Success", f"Welcome {uname}")
                else:
                    messagebox.showerror(
                        "Error", "Incorrect username or password")
            except:
                messagebox.showerror("Error", "No registered user")
        else:
            messagebox.showerror(title="Error",
                                 message="Username and password cannot be empty")


class RegisterWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x832")
        self.master.title("Face Recognition Student Identifier")
        self.master.configure(bg="#fff")
        self.canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=832,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            640.0,
            0.0,
            1280.0,
            832.0,
            fill="#FFFFFF",
            outline="")

        self.image_image_1 = PhotoImage(
            file=frame5("image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            38.0,
            416.0,
            anchor="nw",
            text="Face Recognition Student Identifier",
            fill="#FFFFFF",
            font=("OpenSansRoman Bold", 32 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=frame5("image_2.png"))
        self.image_2 = self.canvas.create_image(
            959.0,
            296.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=frame5("image_3.png"))
        self.image_3 = self.canvas.create_image(
            959.0,
            405.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=frame5("image_4.png"))
        self.image_4 = self.canvas.create_image(
            959.0,
            514.0,
            image=self.image_image_4
        )

        self.entry_image_1 = PhotoImage(
            file=frame5("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            959.5,
            296.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman Regular", 18 * -1)
        )
        self.entry_1.place(
            x=779.0,
            y=275.0,
            width=361.0,
            height=41.0
        )

        self.entry_image_2 = PhotoImage(
            file=frame5("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            959.5,
            405.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman Regular", 18 * -1),
            show="•"
        )
        self.entry_2.place(
            x=779.0,
            y=384.0,
            width=361.0,
            height=41.0
        )

        self.entry_image_3 = PhotoImage(
            file=frame5("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            959.5,
            514.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("OpenSansRoman Regular", 18 * -1),
            show="•"
        )
        self.entry_3.place(
            x=779.0,
            y=493.0,
            width=361.0,
            height=41.0
        )

        self.canvas.create_text(
            903.0,
            174.0,
            anchor="nw",
            text="Register",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 30 * -1)
        )

        self.canvas.create_text(
            779.0,
            236.0,
            anchor="nw",
            text="Username",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        self.canvas.create_text(
            779.0,
            345.0,
            anchor="nw",
            text="Password",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        self.canvas.create_text(
            779.0,
            454.0,
            anchor="nw",
            text="Confirm Password",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=frame5("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.register,
            relief="flat"
        )
        self.button_1.place(
            x=741.0,
            y=589.0,
            width=437.0,
            height=69.0
        )

        self.canvas.create_text(
            877.0,
            698.0,
            anchor="nw",
            text="Already have an account?",
            fill="#8E8E8E",
            font=("OpenSansRoman Regular", 14 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=frame5("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.button_2.place(
            x=872.0,
            y=737.0,
            width=175.0,
            height=35.0
        )

    def login(self):
        newWindow = Tk()
        newWindow.resizable(False, False)
        self.app = MainWindow(newWindow)
        newWindow.destroy()

    def register(self):
        uname = self.entry_1.get()
        pword = self.entry_2.get()
        conpword = self.entry_3.get()
        c = checkRegister(uname, pword, conpword)
        if c == True:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40), password VARCHAR(40))")
            db.commit()
            cursor.execute(f"SELECT * FROM users WHERE username = '{uname}'")
            result = cursor.fetchone()
            if result == None:
                try:
                    cursor.execute(
                        f"INSERT INTO users (username, password) VALUES ('{uname}', '{pword}')")
                    db.commit()
                    messagebox.showinfo(
                        title="Success", message="Registration successful")
                except mysql.connector.Error as err:
                    messagebox.showerror(title="Error", message=str(err))
            else:
                messagebox.showerror("Error", "Username already exists")

        else:
            print("fail")


window = Tk()
app = MainWindow(window)
window.resizable(False, False)
window.mainloop()