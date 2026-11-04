import os
import views as views
import tkinter as tk
import models as models
import sqlite3 as sqlite
from pathlib import Path


def main():
    journal_path = Path.home() / "Documents" / "journal_data"
    journal_path.mkdir(parents=True, exist_ok=True)
    models.general_path = str(journal_path)
    views.window_init()

if __name__ == "__main__":
    main()
