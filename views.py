import tkinter
from tkinter import messagebox

from models import User
from models import Note
from models import viewWindow
from models import userService
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


user_service = userService()

def window_init():
    root = tk.Tk()
    main_menu(root)
    viewWindow(root)._window.geometry("1200x700")  # Set a default size for the window
    viewWindow(root).center_window() # Center the window after it's created
    root.focus_force()  # Ensure the window is focused
    root.mainloop()

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def back_button(parent, command):
    tk.Button(parent, text="<", width=2, command=command).pack(anchor="w", padx=5, pady=5)


#Initial UI which appears when the app is opened.
def main_menu(root):
    clear_window(root)
    frame = ttk.Frame(root) 


    root.title("Reflect")

    tk.Label(frame, text="Reflect", font=("Helvetica", 24)).pack()

    login_btn = tk.Button(frame, text="Login", command=lambda: user_login(root))
    login_btn.focus()
    create_account_btn = tk.Button(frame, text="Create Account", command=lambda: user_creation(root))

    login_btn.pack(pady=10)
    create_account_btn.pack(pady=10)
    frame.pack()


#The main menu the user is going to be on when they are logged in.
def user_select_menu(root, user):
    clear_window(root)
    back_button(root, lambda: main_menu(root))
    frame = ttk.Frame(root)

    root.title("Private Journal")
    
    tk.Label(frame, text=f"Greetings {user.get_pref_name()}!", font=("Helvetica", 18)).pack()

    tk.Button(frame, text="Create a New Journal Entry", command=lambda: create_journal_entry(root, user)).pack()
    tk.Button(frame, text="View your Journal Entries", command=lambda: view_journal_entries(root, user)).pack()
    tk.Button(frame, text="Daily Mood Check-In", command=lambda: daily_mood_checkin(root, user)).pack()

    tk.Button(frame, text="Logout", command=lambda: main_menu(root)).pack()
    frame.pack()


    
#The UI for the user to input the details of their journal entry. User can access this view from the user_select_menu view.
def create_journal_entry(root, user):
    title_var = tk.StringVar()
    clear_window(root)
    frame = ttk.Frame(root)
    root.title("Create Journal Entry")
    back_button(frame, lambda: user_select_menu(root, user))

    journal_title = tk.Entry(frame, width=40, textvariable=title_var)
    journal_title.focus()

    journal_body = scrolledtext.ScrolledText(frame, width=40, height=10)

    tk.Button(frame, text="Save Entry", command=lambda: Note.new_note(Note(user, journal_title.get(), journal_body.get("1.0", tk.END), None), user.get_user_id())).pack()

    journal_title.pack(pady=5)
    journal_body.pack(pady=5)
    frame.pack()



def view_journal_entries(root, user):
    clear_window(root)
    frame = ttk.Frame(root)
    root.title("View your Journal Entries")
    back_button(frame, lambda: user_select_menu(root, user))
    journal_listbox = tk.Listbox(frame, width=50, height=10)
    for entry in user.get_user_entries():
        journal_listbox.insert(tk.END, f"{entry[0]}: {entry[1][:30]}...")  # Display title and first 30 characters of body
    journal_listbox.pack(pady=5)
    frame.pack()

def view_journal_entry_detail(root, user, entry):
    clear_window(root)
    frame = ttk.Frame(root)
    root.title(f"entry[0]")

    entry_title = tk.Label(frame, text=f"Title: {entry[0]}", font=("Helvetica", 14))

    entry_title.pack(pady=5)

    frame.pack()



def daily_mood_checkin(root, user):
    clear_window(root)
    root.title("Daily Mood Check-In")
    back_button(root, lambda: user_select_menu(root, user))

def user_creation(root):
    clear_window(root)
    root.title("Create Account")
    back_button(root, lambda: main_menu(root))

    tk.Label(root, text="Create Account", font=("Helvetica", 18)).pack()

    tk.Label(root, text="Username:").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Email:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Preferred Name:").pack()
    pref_name_entry = tk.Entry(root)
    pref_name_entry.pack()

    tk.Label(root, text="Password:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()\

    tk.Label(root, text="Confirm Password:").pack()
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack()


    tk.Button(root, text="Create Account", command=lambda: create_account(root, username_entry.get(), email_entry.get(), pref_name_entry.get(), password_entry.get())).pack()

    def create_account(root, username, email, pref_name, password):
        if User.confirm_password(password_entry.get(), confirm_password_entry.get()):
            new_user = User(username, email, pref_name, password)
            user_service.add_user(new_user)
            messagebox.showinfo(
                "Account created",
                f"Your user ID is:\n{new_user.user_id}\n\nUse it to log in.",
            )
            main_menu(root)
        else:
            tk.Label(root, text="Passwords do not match. Please try again.", fg="red").pack()
        


def user_login(root):
    clear_window(root)
    frame = ttk.Frame(root)
    root.title("Login")
    back_button(root, lambda: main_menu(root))

    tk.Label(frame, text="Email:").pack()
    email_entry = tk.Entry(frame)
    email_entry.focus()
    email_entry.pack()

    tk.Label(frame, text="Password:").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack()

    def login():
        email = email_entry.get()
        password = password_entry.get()
        user = user_service.authenticate_user(email, password)
        if user is not None:
            user_select_menu(root, user)
        else:
            tk.Label(root, text="Invalid username or password. Please try again.", fg="red").pack()

    tk.Button(frame, text="Login", command=login).pack()
    frame.pack()





if __name__ == "__main__":
    root = tk.Tk()
    main_menu(root)
    #viewWindow(root).fit_window()  # Fit the window to its content
    viewWindow(root)._window.geometry("1200x700")  # Set a default size for the window
    viewWindow(root).center_window() # Center the window after it's created
    root.focus_force()  # Ensure the window is focused
    root.mainloop()
