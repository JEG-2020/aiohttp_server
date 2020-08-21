#!/usr/bin/env python3

"""
These are routes that are available to our aiohttp web server
"""

from aiohttp import web
import app.views as views # This is the file we are going to create next

def setup(app):
    app.add_routes(
        [
            web.get("/health", views.health),
            web.get("/environment", views.environment),
            web.get("/notify", views.notify)
        ]
    )


