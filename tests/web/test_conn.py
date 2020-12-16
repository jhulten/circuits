#!/usr/bin/env python
try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection  # NOQA

import pytest

from circuits.web import Controller


class Root(Controller):

    def index(self):
        return "Hello World!"


@pytest.mark.skip
def test(webapp):
    connection = HTTPConnection(webapp.server.host, webapp.server.port)
    connection.auto_open = False
    connection.connect()

    for i in range(2):
        connection.request("GET", "/")
        response = connection.getresponse()
        assert response.status == 200
        assert response.reason == "OK"
        s = response.read()
        assert s == b"Hello World!"

    connection.close()
