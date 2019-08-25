"""
WSGI config for conf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import cherrypy
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from paste.translogger import TransLogger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animehub.settings.dev")

app = get_wsgi_application()
logged_app = TransLogger(app, format=None, setup_console_handler=True)

# Prevent cherrypy from automatically reloading.
cherrypy.config.update({'global': {'engine.autoreload.on': False}})


static_config = {
    'tools.staticdir.on': True,
    'tools.staticdir.dir': settings.STATIC_ROOT
}

# Mount the application
cherrypy.tree.mount(None, settings.STATIC_URL, {'/': static_config})
cherrypy.tree.graft(logged_app, "/")

# Unsubscribe the default server
cherrypy.server.unsubscribe()

# Instantiate a new server object
server = cherrypy._cpserver.Server()

# Configure the server object
server.socket_host = "0.0.0.0"
server.socket_port = int(os.environ.get('PORT', 8080))
server.thread_pool = 30

cherrypy.log.screen = True

# Subscribe this server
server.subscribe()

cherrypy.engine.start()
cherrypy.engine.block()
