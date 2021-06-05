#!/usr/bin/python3
"""Unittest foralmost a circle / base
"""
import unittest
import os

import models.base
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to test the base class"""

    # Testing pep8 and shebang
    def test_pep8(os_system):
        """testing style"""
        os_system.assertEqual(os.system("pep8 ./models/base.py"), 0)

    def test_shebang(self):
        """Testing the shebang"""
        with open('./models/base.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Function to test if have module documentation"""
        temp = models.base.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Function to test if have class documentation"""
        temp = Base.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docfunction(self):
        """Function to test if have function documentation"""
        temp = Base.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
