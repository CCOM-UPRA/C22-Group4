from flask import session

# This is a very basic dictionary with information for logging in
# Simulating our database
thisDict = {
    "email": ["javier.quinones3@upr.edu", "joseph1@upr.edu"],
    "password": ["pass1234", "Lia1"],
    "user": ["Javier", "Joseph"]
}


def setDicList(email, password):
    thisDict.get("email").append(email)
    thisDict.get("password").append(password)
    thisDict.get("user").append(email[0:5])


def loginmodel(email, password, flag):
    if flag:
        flag = False
        setDicList(email, password)

    for i in range(len(thisDict.get("email"))):
        # Receive email and password to check in the "database"
        if email in thisDict.get("email")[i] and password in thisDict.get("password")[i]:
            # If it found the email and pass in the dictionary
            session['customer'] = thisDict.get("user")[i]
            # Create the session['customer']
            return "true"
    return "false"

def getdict():
    return thisDict