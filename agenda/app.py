#!/usr/bin/env python3

"""Simple Flask application."""

from flask import Flask
from flask_httpauth import HTTPBasicAuth
import sqlite3
import logging


LOG = logging.getLogger(__name__)

def init():
    """Initialise a SQLite database."""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Drop table if it exists
    c.execute('DROP TABLE IF EXISTS users')

    # Create table
    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Insert two users
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", ('User 1', 'user1@example.com', 'user1secret'))
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", ('User 2', 'user2@example.com', 'thisisverysecret'))
    
    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()


def main():
    """Command-line entry point."""
    app = Flask(__name__)
    auth = HTTPBasicAuth()

    logging.basicConfig(level=logging.DEBUG)

    @auth.verify_password
    def verify_password(name: str, password: str) -> bool:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE name = ?', (name,))
        user = c.fetchone()
        conn.close()
        if user is None:
            LOG.debug('User not found: %s, with password: %s', name, password)
            return False
        return user[3] == password


    @app.route('/')
    def home():
        return "Hello, World!"


    @auth.login_required
    @app.route('/query-by-name/<name>')
    def query_name(name: str):
        """Get info for an user by name."""
        user = auth.current_user()
        if user.name != name:
            return "Unauthorized", 403

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE name = ' + name)
        user = c.fetchone()
        conn.close()
        return str(user)


    @app.route('/query-by-email/<email>')
    def query_email(email: str):
        """Get info for an user by email."""
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?', [email])
        user = c.fetchone()
        conn.close()
        return str(user)


    @auth.login_required
    @app.route('/query-by-id/<id>')
    def query_id(id: str):
        """Get info for an user by id."""
        user = auth.current_user()
        if user.id != id:
            return "Unauthorized", 403
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE id = ' + id)
                user = c.fetchone()
        conn.close()
        return str(user)

    init()
    app.run(debug=True)


if __name__ == '__main__':
    main()