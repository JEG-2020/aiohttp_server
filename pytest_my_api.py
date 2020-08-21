#!/usr/bin/env python3

"""
This script tests the my_api code.
"""

import requests
import json
import datetime

TODAY = datetime.datetime.today()

def test_yesterday():
    r = requests.get("http://localhost:9999/api/v1/yesterday")
    # Make sure the status returned is 200
    assert r.status_code == 200

    # Make sure there is JSON data in the response
    assert r.json()

    # Make sure the JSON data has the "yesterday" key
    assert r.json().get("yesterday") is not None

    # Make sure that the value of "yesterday" is accurate
    yesterday = TODAY - datetime.timedelta(days=1)
    assert r.json().get("yesterday") == yesterday.strftime("%Y-%d-%m")


def test_days_ago():
    n = 5
    r = requests.get(f"http://localhost:9999/api/v1/ago/{n}")
    # Make sure the status returned is 200
    assert r.status_code == 200

    # Make sure there is text data in the response
    assert r.text
    
    # Make sure the value of "n days ago" is accurate 
    days_ago = TODAY - datetime.timedelta(days=n)
    assert r.text == f"{n} days ago was {days_ago.strftime('%A %B %dth %Y')}"
    
    
if __name__ == "__main__":
    test_yesterday()
    test_days_ago()

