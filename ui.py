from models import User
from models import Notes
import tkinter as tk

def main_menu():
    root = tk.Tk()
    root.title("Reflect")
    print("Welcome to Reflect")
    print("1. Create new account")
    print("2. Log in to existing account")
    if (user := input("Enter your choice (1 or 2): ")) == "1":
        user_creation()
    if (user := input("Enter your choice (1 or 2): ")) == "2":
        user_login()

def user_creation():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    pref_name = input("Enter your preferred name: ")
    password = input("Enter your password: ")
    User(username, email, pref_name, password)
    print("Account created successfully!")
    main_menu()

def user_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Here you would typically check the credentials against stored user data
    print(f"Welcome back, {username}!")
    main_menu()