#!/usr/bin/env python

import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
from http.cookiejar import CookieJar

import pytest

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        pytest.skip("Skip: No JSON support")

from circuits.web import JSONController, Sessions

class Root(JSONController):

    def index(self):
        return {"success": True, "message": "Hello World!"}

    def test_sessions(self, name=None):
        if name:
            self.session["name"] = name
        else:
            name = self.session.get("name", "World!")

        return {"success": True, "message": "Hello %s" % name}

def test(webapp):
    f = urlopen(webapp.server.base)
    data = f.read()
    d = json.loads(data)
    assert d["success"]
    assert d["message"] == "Hello World!"

def test_sessions(webapp):
    Sessions().register(webapp)

    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    f = opener.open("%s/test_sessions" % webapp.server.base)
    data = f.read()
    d = json.loads(data)
    assert d["success"]
    assert d["message"] == "Hello World!"

    f = opener.open("%s/test_sessions/test" % webapp.server.base)
    data = f.read()
    d = json.loads(data)
    assert d["success"]
    assert d["message"] == "Hello test"

    f = opener.open("%s/test_sessions" % webapp.server.base)
    data = f.read()
    d = json.loads(data)
    assert d["success"]
    assert d["message"] == "Hello test"
