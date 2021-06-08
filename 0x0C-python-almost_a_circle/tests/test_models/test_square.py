#!/usr/bin/python3
"""Unittest for almost a circle / Square
"""
import unittest
import io
import sys
import os

import models.square
from models.square import Square
from models.base import Base


class Test_Square_Requeriments(unittest.TestCase):
    """Class to test the Square class requeriments"""

    # Testing pep8 and shebang
    def test_pep8(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/square.py"), 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/square.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.square.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = Square.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_getters(self):
        """Functions getter are documented"""
        # Getters
        temp = Square.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Square.size.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_methods(self):
        """Functions are documented"""
        # Str
        temp = Square.__str__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Update
        temp = Square.update.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


class Test_Square(unittest.TestCase):
    """Class to test the Square class funcionalities"""

    def setUp(self):
        """setup nb_objectes to 0 after each test"""
        Base._Base__nb_objects = 0

    # Task 10. And now, the Square! str
    def test_str_square(self):
        """Correct output"""
        s1 = Square(5)
        test1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(s1.__str__(), test1)

        s2 = Square(2, 2)
        test1 = '[Square] (2) 2/0 - 2'
        self.assertEqual(s2.__str__(), test1)

        s3 = Square(3, 1, 3)
        test1 = '[Square] (3) 1/3 - 3'
        self.assertEqual(s3.__str__(), test1)

    # Task 10. And now, the Square! area
    def test_area_square(self):
        """correct output"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    # Task 10. And now, the Square! display
    def test_display_square(self):
        """Correct output in stdout"""
        s1 = Square(5)
        s1_str = "#####\n#####\n#####\n#####\n#####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), s1_str)
        captured_output.flush()

        s2 = Square(2, 2)
        s2_str = "  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), s2_str)

        s3 = Square(3, 1, 3)
        s3_str = "\n\n\n ###\n ###\n ###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), s3_str)

    # Task 11. Square size
    def test_size(self):
        """Correct output"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    # Task 12. Square update
    def test_update_square(self):
        """Correct Output"""
        s1 = Square(5)
        test1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(s1.__str__(), test1)

        s1.update(10)
        test1 = '[Square] (10) 0/0 - 5'
        self.assertEqual(s1.__str__(), test1)

        s1.update(1, 2)
        test1 = '[Square] (1) 0/0 - 2'
        self.assertEqual(s1.__str__(), test1)

        s1.update(1, 2, 3)
        test1 = '[Square] (1) 3/0 - 2'
        self.assertEqual(s1.__str__(), test1)

        s1.update(1, 2, 3, 4)
        test1 = '[Square] (1) 3/4 - 2'
        self.assertEqual(s1.__str__(), test1)

        s1.update(x=12)
        test1 = '[Square] (1) 12/4 - 2'
        self.assertEqual(s1.__str__(), test1)

        s1.update(size=7, y=1)
        test1 = '[Square] (1) 12/1 - 7'
        self.assertEqual(s1.__str__(), test1)

        s1.update(size=7, id=89, y=1)
        test1 = '[Square] (89) 12/1 - 7'
        self.assertEqual(s1.__str__(), test1)

    #T ask 14. Square instance to dictionary representation
    def test_to_dict_square(self):
        """Correct Output"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        test1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, test1)
        self.assertIsInstance(s1_dictionary, dict)

        s2 = Square(1, 1)
        self.assertNotEqual(s1.__str__(), s2.__str__())
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        test2 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s2_dictionary, test2)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertIsNot(s1.__str__(), s2.__str__())
