# Description: The following function contains bugs thus not returning the desired outupt with given test parameters. Find all bugs and fix it. The function should return a random 256-bit hex string if the username and password match the database and save the token into session_tokens with the token being the key and username as the value. If user does not exist or password is incorrect, raise a ValueError with a short error message.

import random

database = {
    "users": {
        # username: password
        "adam": "1234",
        "peter": "asdf5678",
        "joe": "password123",
        "john": "_john97!",
        "criag": "superman732",
        "michael": "letmein_123@",
    }
}

session_tokens = {
    # token: username
}

def login(user: str, password: str) -> str:
    if user not in user:
        raise ValueError("User does not exist")
    
    if password != database[user]:
        return "Incorrect password"
    
    token = ""
    while token in session_tokens:
        random.randbytes(256).hex()

    session_tokens[token] = user

    return token

# Tests
print(login("adam", "1234")) # random 256-bit hex string
print(login("peter", "my-invalid-password")) # ValueError: Incorrect password
print(login("johnathan", "_john97!")) # ValueError: User does not exist