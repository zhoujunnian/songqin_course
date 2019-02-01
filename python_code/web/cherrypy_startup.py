HOST        = '0.0.0.0'
PORT        = 80
THREAD_POOL = 10

import sys,os

sys.path.insert(0,os.getcwd())

from wsgi import application
import cherrypy 


# Mount the application
cherrypy.tree.graft(application, "/")

# Unsubscribe the default server
cherrypy.server.unsubscribe()

# Instantiate a new server object
server = cherrypy._cpserver.Server()
server.socket_host = HOST
server.socket_port = PORT
server.thread_pool = THREAD_POOL
server.subscribe()


cherrypy.engine.start()
cherrypy.engine.block()

