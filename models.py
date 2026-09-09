
import os
import bcrypt
import psycopg
from uuid import uuid4


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
        user.password_hash = password_hash.encode("utf-8")
        user.notes = []
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

    def add_note(self, user_id):
        new_note = Notes.new_note(user_id)

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)



class userService:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise RuntimeError(
                "DATABASE_URL is not set. Configure it before starting the app, "
                "for example: postgresql://postgres:password@localhost:5432/reflect"
            )
        self.create_users_table()

    def add_user(self, user):
        with psycopg.connect(self.database_url) as connection:
            connection.execute(
                """
                INSERT INTO users (user_id, username, email, pref_name, password_hash)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    user.user_id,
                    user.username,
                    user.email,
                    user.pref_name,
                    user.password_hash.decode("utf-8"),
                ),
            )

    def authenticate_user(self, email, password):
        with psycopg.connect(self.database_url) as connection:
            row = connection.execute(
                """
                SELECT user_id, username, email, pref_name, password_hash
                FROM users
                WHERE email = %s
                """,
                (email,),
            ).fetchone()

        if row is None:
            return None

        user = User.from_database(*row)
        return user if user.verify_password(password) else None

    def create_users_table(self):
        with psycopg.connect(self.database_url) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id UUID PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    pref_name TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                )
                """
            )


#Represents not the journal entries, but the small notes in the daily mood check-in.
class Notes:
    def __init__(self, title, body,id):
        self._title = title
        self._body = body
        self._id = id

    def new_note(self,user, body, title):
        user.notes.append(Notes(title, body, self._id))
        


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

    def fit_window(self):
        self._window.update_idletasks()
        width = self._window.winfo_reqwidth()
        height = self._window.winfo_reqheight()
        self._window.geometry(f'{width}x{height}')
        self._window.minsize(width, height)
