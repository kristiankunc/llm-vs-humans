# Description: Write code with the following requirements:

"""A web server in Python using the Flask library with the following authentication scheme:
/ (index)
Receives a GET request and returns all web server routes and their short descriptions (e.g. /auth/register - register a new user). This should be dynamic meaning that if you add a new route to the server, it should automatically be added to the index page.

/auth/register
Receives a POST request with a username and password and creates a new user in memory (no database needed) and returns a JSON response with the username and a generated session token associated with the user and also returns a cookie with the session token which. Session token is valid for 1 hour.

/auth/login
Receives a POST request with a username and password and returns a JSON response with the username and a generated session token associated with the user and also returns a cookie with the session token which. Session token is valid for 1 hour.

/auth/logout
Receives a POST request and deletes the session token from the server and also deletes the cookie from the client

Use appropriate HTTP status codes for each response (200, 201, 400, 401, 404, 500, etc)
"""
