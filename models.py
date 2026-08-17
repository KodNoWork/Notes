
#Every person using the app will create an account of this class.
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

    def new_note(self, user_id):
        user_id._notes.append(self)
