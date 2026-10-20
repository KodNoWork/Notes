import os as os
import bcrypt
from uuid import uuid4
import sqlite3 as sqlite



class User:
    def __init__(self, username,email,pref_name, password):
        self.user_id = str(uuid4())
        self.username = username
        self.email = email
        self.pref_name = pref_name
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.notes = []

    def get_pref_name(self):
        return self.pref_name

    @classmethod
    def from_database(cls, user_id, username, email, pref_name, password_hash):
        user = cls.__new__(cls)
        user.user_id = str(user_id)
        user.username = username
        user.email = email
        user.pref_name = pref_name
        user.password_hash = password_hash.encode('utf-8') if isinstance(password_hash, str) else password_hash
        return user

    def change_username(self, new_username):
        self.username = new_username

    def change_password(self, new_password):
        self.password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    def confirm_password(password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False

    def change_email(self, new_email):
        self.email = new_email

    def add_note(self, title, body):
        self.notes.append(Note(title, body, len(self.notes) + 1))   
        

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def identify_user_by_id(self, user_id):
        return self.user_id == user_id


class userService:
    def __init__(self):
        os.chdir("/home/filip/Documents/journal_data") if os.path.exists("/home/filip/Documents/journal_data") else os.mkdir("/home/filip/Documents/journal_data")
        self.conn = sqlite.connect("/home/filip/Documents/journal_data/users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (user_id TEXT PRIMARY KEY,
                                username TEXT,
                                email TEXT,
                                pref_name TEXT,
                                password_hash TEXT)''')
        self.conn.commit()

    def add_user(self, user):
        self.cursor.execute('''INSERT INTO users (user_id, username, email, pref_name, password_hash)
                               VALUES (?, ?, ?, ?, ?)''', (user.user_id, user.username, user.email, user.pref_name, user.password_hash))
        self.conn.commit()

    def authenticate_user(self, email, password):
        self.cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
        user_data = self.cursor.fetchone()
        if user_data:
            user = User.from_database(*user_data)
            if user.verify_password(password):
                return user
        return None


#Represents not the journal entries, but the small notes in the daily mood check-in.
class Note:
    def __init__(self, title, body,id):
        self._title = title
        self._body = body
        self._id = id
    
    def new_note(user_id,title,body):
        user_id.add_note(title, body)
        
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

  
