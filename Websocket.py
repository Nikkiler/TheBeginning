import eventlet
import socketio
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)