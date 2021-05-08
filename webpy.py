import json
def get_stored_username():
 """Get stored username if available."""

def get_new_username():
 """Prompt for a new username."""
 username = input("What is your name? ")
 filename = 'username.json'
 with open(filename, 'w') as f_obj:
      json.dump(username, f_obj)
 return username
     

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
 
 
 if username:
     print("Welcome back, " + username + "!")
     
     
 
 else:
      username = get_new_username()
 print("We'll remember you when you come back, " + username + "!")
     

greet_user()
    
 
