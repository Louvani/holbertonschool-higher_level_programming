#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer functión"""

    def test_maxinteger(self):
        """Function to test the max integer"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([-8, -9, -3, -5, -10]), -3)
        self.assertAlmostEqual(max_integer([15]), 15)
        self.assertAlmostEqual(max_integer([15, 1024, 3568]), 3568)

    def test_emptylist(self):
        """Function to test if return None if list is empty"""
        # self.assertAlmostEqual(max_integer([]), None)
        self.assertEqual(max_integer([]), None)

    def test_bignumber(self):
        """Function to test max integer with big numbers"""
        self.assertAlmostEqual(max_integer(
            [4748178714196817229795479548954972,
                5972197291279179219731929457954975497591729]),
                5972197291279179219731929457954975497591729)

    def test_types(self):
        """Function to test if raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer("Holberton")
            max_integer(True)
            max_integer((1, 2))
            max_integer([1, 3.5, 6])

    def test_docmodule(self):
        """Function to test if have module documentation"""
        temp = __import__('6-max_integer').__doc__
        self.assertTrue(temp is not None and len(temp) > 5)

    def test_docfunction(self):
        """Function to test if have function documentation"""
        temp = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(temp is not None and len(temp) > 5)

if __name__ == '__main__':
    unittest.main()
