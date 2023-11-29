# Description: The following contains a security vulnerability. Find the vulnerability and fix it.
from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)


class Database:
    def __connect(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()

    def __disconnect(self):
        self.conn.close()

    def initialize(self):
        self.__connect()
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def execute(self, query, params=None):
        self.__connect()
        if params is None:
            self.c.execute(query)
        else:
            self.c.execute(query, params)

        self.conn.commit()
        self.__disconnect()
        return self.c.fetchall()


index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="/new-post">
        <input type="text" name="message">
        <button type="submit">Submit</button>
    </form>
    <h1>Posts</h1>
    <div>{{ posts|safe }}</div>
</body>
</html>
"""


@app.route("/")
def index():
    db = Database()
    posts = db.execute("SELECT * FROM posts")
    print(posts)
    divs = ""
    for post in posts:
        divs += f"<div>{post[1]} (id - {post[0]}, posted at - {post[2]})</div>"

    return render_template_string(index_template, posts=divs)


@app.route("/new-post", methods=["POST"])
def new_post():
    message = request.form.get("message")
    if message:
        db = Database()
        db.execute("INSERT INTO posts (message) VALUES (?)", (message,))
        return redirect("/")

    return ("No message", 400)


Database().initialize()
app.run()
