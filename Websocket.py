import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.enter_room(sid, 'Chat')
    sio.emit('menu')


@sio.event
def Message(sid, data):
    print('message ', data)
    sio.emit('Message', data, room='Chat', skip_sid=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)