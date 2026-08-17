from models import User
from models import Notes
import tkinter as tk

def main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Reflect")

    tk.Label(root, text="Reflect", font=("Helvetica", 24)).pack()

    tk.Button(root, text="Create Account", command=lambda: user_creation(root)).pack()
    tk.Button(root, text="Login", command=lambda: user_login(root)).pack()


def user_creation(root):
    for widget in root.winfo_children():
        widget.destroy()

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


    #TODO: Implement user having to enter username, email and preferred name aswell. 
    #TODO: Implement user having an option to return to the mainmenu if they accidentally click create account.
    #TODO: Do i really need the users email? ig it might be a good idea to have it for account recovery.
    def create_account(root, username, email, pref_name, password):
        if User.confirm_password(password_entry.get(), confirm_password_entry.get()):
            new_user = User(username, email, pref_name, password)
            print(f"Account created for {new_user._username}!")
            main_menu(root)
        else:
            tk.Label(root, text="Passwords do not match. Please try again.", fg="red").pack()
        




def user_login(root):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Here you would typically check the credentials against stored user data
    print(f"Welcome back, {username}!")



if __name__ == "__main__":
    root = tk.Tk()
    main_menu(root)
    root.mainloop()
