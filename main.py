import os



def main():
    print("Welcome to the notes app!")


def create_quick_note():
    title = input("Enter the title of the note: ")
    body = input("Enter the body of the note: ")    
    with open(f"{title}.txt", "w") as file:
        file.write(body)
    print(f"Note '{title}' created successfully!")

def view_quick_notes():
    for filename in os.listdir("."):
        if filename.endswith(".txt"):
            with open(filename, "r") as file:
                print(file.read())

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.notes = []

    def create_user(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.email = input("Enter your email: ")
        self.phone_number = input("Enter your phone number: ")

    def add_note(self, note):
        self.notes.append(note)

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        for note in self.notes:
            print(f"Title: {note.title}\nBody: {note.body}\n")


class Note:
    def __init__(self, title, body,id):
        self.title = title
        self.body = body
        self.id = id
