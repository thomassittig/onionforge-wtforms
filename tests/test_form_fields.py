# -*- coding: utf-8 -*-
""" unit, functional and integration tests for admin/user_login-view
"""

import unittest, os, mox
import onionforge_wtforms.fields as fields

from jhi_tools import enum

class FooBar(enum.enumerated):
    FOO = enum.enum()
    BAR = enum.enum()

class FooForm(fields.wtforms.Form):
    foo = fields.EnumSelectField(FooBar)

class EnumSelectFieldTests(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_instanciate(self):
        form = FooForm()
        self.assertEqual(len(form.foo.choices), 2)

    def test_choices(self):
        form = FooForm()

        self.assertEqual(form.foo.choices[0][0], "0")
        self.assertEqual(form.foo.choices[0][1], "FooBar.FOO")

        self.assertEqual(form.foo.choices[1][0], "1")
        self.assertEqual(form.foo.choices[1][1], "FooBar.BAR")

    def test_data_as_constant(self):
        form = FooForm(foo=1)
        self.assertEqual(form.foo.as_constant(), FooBar.BAR)

    def test_request_as_constant(self):
        from webob.multidict import MultiDict

        form = FooForm(MultiDict({"foo":"1"}))
        self.assertEqual(form.foo.as_constant(), FooBar.BAR)



