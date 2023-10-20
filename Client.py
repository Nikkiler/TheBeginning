import socketio

sio = socketio.Client()


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
    print("1. Login")
    print("2. Send a message")
    choice = int(input())
    while choice != 1 and choice != 2:
        print("Choose 1 or 2")
        choice = int(input())
    if choice == 1:
        print('Feature Unavailable at the moment')
    elif choice == 2:
        print('What would you like to send to the server?')
        message = input()
        sio.emit('Message', message)


sio.connect('http://localhost:5001')
sio.wait()
