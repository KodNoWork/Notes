import os
import views as views
import tkinter as tk
import models as models
import sqlite3 as sqlite


def main():
    os.mkdir("/home/filip/Documents/journal_data") if not os.path.exists("/home/filip/Documents/journal_data") else None
    if os.path.exists("/home/filip/Documents/journal_data"):
        journal_path = "/home/filip/Documents/journal_data"
    
    
    


if __name__ == "__main__":
    main()
    views.window_init()