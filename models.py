
#Every person using the app will create an account of this class.
from curses import window
from turtle import width


class User:
    def __init__(self, username,email,pref_name, password):
        self._username = username
        self._email = email
        self._pref_name = pref_name
        self._password = password
        self._notes = []
        self._id = 000000

    def change_username(self, new_username):
        self._username = new_username

    def change_password(self, new_password):
        self._password = new_password

    def confirm_password(password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False

    def change_email(self, new_email):
        self._email = new_email

    def add_note(self, user_id):
        new_note = Notes.new_note(user_id)


#Represents not the journal entries, but the small notes in the daily mood check-in.
class Notes:
    def __init__(self, title, body,id):
        self._title = title
        self._body = body
        self._id = id

    def new_note(self, body, title):
        self._notes.append(Notes(title, body, self._id))
        


#Centers the tkinter windows fron views on the screen.
#TODO: Make this happen before the window appears on the screen, not after.
class viewWindow:
    def __init__(self, window):
        self._window = window
        
    def center_window(self):
        self._window.update_idletasks()
        width = self._window.winfo_width()
        height = self._window.winfo_height()
        x = (self._window.winfo_screenwidth() // 2) - (width // 2)
        y = (self._window.winfo_screenheight() // 2) - (height // 2)
        self._window.geometry(f'{width}x{height}+{x}+{y}')
