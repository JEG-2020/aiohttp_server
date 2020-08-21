#!/usr/bin/env python

"""
This is the main process for the aiohttp server.

This works by instantiating the app as a web.Application(),
then applying the setup function we built in our app.routes
file to add routes to our app, then by starting the async
event loop with web.run_app().
"""

from aiohttp import web
import app.routes as routes

if __name__ == "__main__":
    print("This aiohttp web server is starting up!")
    app = web.Application()
    routes.setup(app)
    web.run_app(app, port=54321)

