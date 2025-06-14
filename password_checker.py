my_password = "hit_me"

def password_checker(text):
    if text == my_password:
        print("Successfully logged in!")
    else:
        print("Incorrect Password")
        
password_checker("hit_me")