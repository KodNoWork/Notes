import os
import views
import tkinter as tk
import models as models
import sqlite3 as sqlite
from pathlib import Path


def main():
    journal_path = Path.home() / "Documents" / "journal_data"
    journal_path.mkdir(parents=True, exist_ok=True)
    models.set_journal_path(journal_path)
    user_service = models.userService()
    models.set_user_service(user_service)
    views.window_init()

if __name__ == "__main__":
    main()
