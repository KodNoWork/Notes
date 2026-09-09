Daily mood tracker/journal app using Python and tkinter for the ui. First attempt at this, aiming to make this for personal use after annoyance using available apps on the app store, riddled with ads and ludicrous payment options.

## Local PostgreSQL setup

Install the PostgreSQL driver:

```bash
pip install psycopg[binary]
```

Create a local database, then set its connection string before starting the app:

```bash
sudo -u postgres createdb reflect
export DATABASE_URL="postgresql://postgres:your_password@localhost:5432/reflect"
python views.py
```

The app creates the `users` table automatically. Passwords are stored as bcrypt
hashes, and each account's UUID is stored in the `user_id` column.
