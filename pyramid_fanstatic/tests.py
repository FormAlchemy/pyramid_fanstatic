# -*- coding: utf-8 -*-

import unittest

from pyramid import testing
from webtest import TestApp
from js.jquery import jquery


def home(request):
    resp = request.response
    resp.content_type = 'text/html'
    resp.body = '''\
<html>
<head>
</head>
<body>
</body>
</html>
'''
    jquery.need()
    return resp


class TestTween(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include("pyramid_fanstatic")
        self.config.add_route('home', '/')
        self.config.add_view(route_name='home', view=home)
        self.app = TestApp(self.config.make_wsgi_app())

    def test_injector(self):
        resp = self.app.get('/')
        resp.mustcontain(('<script type="text/javascript" '
                          'src="/fanstatic/jquery/jquery.js"></script>'))

    def test_publisher(self):
        resp = self.app.get('/fanstatic/jquery/jquery.js')
        resp.mustcontain('window.jQuery = window.$ = jQuery;')

    def tearDown(self):
        testing.tearDown()


class TestCustomConfig(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.registry.settings.update({
            'fanstatic.publisher_signature': 'custom_sign',
        })
        self.config.include("pyramid_fanstatic")
        self.config.add_route('home', '/')
        self.config.add_view(route_name='home', view=home)
        self.app = TestApp(self.config.make_wsgi_app())

    def test_injector(self):
        resp = self.app.get('/')
        resp.mustcontain(('<script type="text/javascript" '
                          'src="/custom_sign/jquery/jquery.js"></script>'))

    def test_publisher(self):
        resp = self.app.get('/custom_sign/jquery/jquery.js')
        resp.mustcontain('window.jQuery = window.$ = jQuery;')

    def tearDown(self):
        testing.tearDown()
