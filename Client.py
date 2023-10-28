import socketio, csv
users = {}
sio = socketio.Client()
with open("Data.csv", "r") as handler:
    reader = csv.DictReader(handler, delimiter=',')
    for row in reader:
        cr = row['Username']
        users[cr] = row

@sio.event
def connect():
    print('connection established')


@sio.event
def Message(data):
    print('message: ', data)


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def menu():
    options()
    current_user = 'Guest'
    choice = int(input())
    while choice != 1 and choice != 2 and choice != 3:
        print("Choose 1 or 2 or 3")
        choice = int(input())
    if choice == 1:
        current_user = login(users)
        message()
    elif choice == 2:
        current_user = register(users)
        message()
    elif choice == 3:
        message()

def login(users):
    print("please enter username")
    usercheck = input()
    while usercheck not in users:
        print("please enter a created user")
        usercheck = input()
        if usercheck in users:
            print("Welcome " + usercheck + " Please enter you password")
            passcheck = input()
            password = users[usercheck]
            while password["Password"] != passcheck:
                print("Password is incorrect")
                print("Please enter correct password")
                passcheck = input()
            print("Welcome back " + usercheck)
            return usercheck
    if usercheck in users:
        print("Welcome " + usercheck + " Please enter you password")
        passcheck = input()
        password = users[usercheck]
        while password["Password"] != passcheck:
            print("Password is incorrect")
            print("Please enter correct password")
            passcheck = input()
        print("Welcome back " + usercheck)
        return usercheck

def register(username):
    userinput = input("Please, enter the username ")
    while len(userinput) == 0:
        userinput = input("Username is null please enter another name, please enter another name ")
    while userinput in username:
        userinput = input("Username already registered, please enter another name ")
        while len(userinput) == 0:
            userinput = input("Username is null please enter another name, please enter another name ")
    print("Please enter a password for this user:")
    passwords = input()
    print("User " + userinput + " registered")
    username[userinput] = {'Name': userinput, 'Password': passwords}
    with open('Data.csv', 'w') as wf:
        fieldnames = ['Username', 'Password']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in users.items():
            writer.writerow(value)
    return userinput

def options():
    print("1. Login")
    print("2. Register")
    print("3. Send a message")
def message():
    print('What would you like to send to the server?')
    message = input()
    sio.emit('Message', message)
sio.connect('http://localhost:5001')
sio.wait()
