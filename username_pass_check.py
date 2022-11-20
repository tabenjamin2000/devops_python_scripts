### Python script to check user's Username and Password of an application as Username = admin, Password = admin.   
### The code returns to the user "wrong username or password" if the user enters the wrong credentials.

_username = input("Enter your Username: ")
_passwd = input("Enter your Password: ")
if _username == _passwd == "admin":  
    print("Successful login!")
else:
    print("Wrong Credentials. Please check your Username and Password and try again")
