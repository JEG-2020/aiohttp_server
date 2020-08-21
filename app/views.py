#!/usr/bin/env python3

"""
These are the functions that get called when one of the paths mentioned in routes.py is accessed.
"""

"""
All functions that are called from the routes.py
script will need to accept the request as their first parameter.

For right now, we are disregarding the request, but it may be
useful for us when we become more advanced aiohttp users.

The function definition above is "typed". This means that
the function is taking in the parameter named 'healthy', 
which has the "type" of a bool value, which also has a 
default value of True.

Although Python is famous for it's "duck typing" style,
the more advanced Pythoneers will find themselves declaring
types as a way to easily find code errors, prevent themselves
from making them in the first place, and even taking advantage
of advanced syntax checkers.

(If it walks like a duck, and quacks like a duck, it is a duck.)

This function will check if "healthy" is True, and then return a
JSON response. 
"""

import json
import os
from aiohttp import web

async def health(request, healthy: bool = True):
    print(f"A request has come in to /health!\n\n{request}")
    if healthy:
        response = web.HTTPCreated(body=json.dumps({"healthy": True}))
    else:
        response = web.HTTPCreated(body=json.dumps({"healthy": False}))
    return response


async def environment(request):
    """
    This function simply looks at some of the environmental variables
    found within the shell from which this server was launched and 
    returns them to the requester. 
    """

    print(f"A request has come in to /environment!\n\n{request}")
    results = os.environ.get("PWD")
    response = web.Response(text=results)
    return response


async def notify(request):
    """
    This function will be used more later. For right now, we want it 
    to simply return the text "A Notification Has Been Sent"
    """

    print(f"A request has come in to /notify!\n\n{request}")
    response = web.Response(text="A Notification Has Been Sent")
    return response

