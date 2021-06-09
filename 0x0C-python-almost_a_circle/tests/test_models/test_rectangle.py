#!/usr/bin/python3
"""Unittest foralmost a circle / Rectangle
"""
import unittest
import io
import sys
import os

import models.rectangle
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle_Requeriments(unittest.TestCase):
    """Class to test the Rectangle class requeriments"""

    # Testing pep8 and shebang
    def test_pep8(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/rectangle.py"), 0)

    def test_pep8_test_rectangle(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_rectangle.py")
        os_system.assertEqual(path, 0)

    def test_shebang_rectangle(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/rectangle.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_rectangle(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_rectangle.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.rectangle.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = Rectangle.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_getters(self):
        """Functions getter are documented"""
        # Getters
        temp = Rectangle.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.width.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.height.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.x.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        temp = Rectangle.y.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_methods(self):
        """Functions are documented"""
        # Area
        temp = Rectangle.area.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Display rectangle
        temp = Rectangle.display.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Str
        temp = Rectangle.__str__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # Update
        temp = Rectangle.update.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)
        # to_dictionary
        temp = Rectangle.to_dictionary.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


# Test for task 2. First Rectangle
class Test_Rectangle(unittest.TestCase):
    """Class to test the Rectangle class funcionalities"""

    def setUp(self):
        """setup nb_objectes to 0 after each test"""
        Base._Base__nb_objects = 0

    # Task 2
    def test_rectangle_constructor(self):
        """Correct Output"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    # Task 2 how to test if is private atributte?????

    # Task 3. Validate attributes
    def test_validate_types(self):
        """Raise TypeError"""
        self.assertRaisesRegex(
            TypeError, 'width must be an integer', Rectangle, "10", 5)
        self.assertRaisesRegex(
            TypeError, 'height must be an integer', Rectangle, 10, "2")
        self.assertRaisesRegex(
            TypeError, 'x must be an integer', Rectangle, 10, 5, {})
        self.assertRaisesRegex(
            TypeError, 'y must be an integer', Rectangle, 10, 5, 2, 3.5)

    def test_validate_values(self):
        """Raise TypeValue"""
        self.assertRaisesRegex(
            ValueError, 'width must be > 0', Rectangle, 0, 5)
        self.assertRaisesRegex(
            ValueError, 'width must be > 0', Rectangle, -10, 5)
        self.assertRaisesRegex(
            ValueError, 'height must be > 0', Rectangle, 5, 0)
        self.assertRaisesRegex(
            ValueError, 'height must be > 0', Rectangle, 5, -10)
        self.assertRaisesRegex(
            ValueError, 'x must be >= 0', Rectangle, 5, 10, -5)
        self.assertRaisesRegex(
            ValueError, 'y must be >= 0', Rectangle, 5, 10, 15, -8)

    # Task 4. Area first
    def test_area(self):
        """correct output"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # Task 5. Display #0
    def test_display_0(self):
        """Correct output in stdout"""
        r1 = Rectangle(4, 6)
        r1_str = "####\n####\n####\n####\n####\n####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), r1_str)
        captured_output.flush()

        r2 = Rectangle(2, 2)
        r2_str = "##\n##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), r2_str)

    # Task 6. __str__
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    # Task 7. Display #1
    def test_display_1(self):
        """Correct output in stdout"""
        r1 = Rectangle(2, 3, 2, 2)
        r1_str = "\n\n  ##\n  ##\n  ##\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), r1_str)
        captured_output.flush()

        r2 = Rectangle(3, 2, 1, 0)
        r2_str = " ###\n ###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), r2_str)
        captured_output.flush()

        r3 = Rectangle(3, 2, 0, 1)
        r3_str = "\n###\n###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), r3_str)

    # Task 8. Update #0
    def test_update_0(self):
        """Correct Output"""
        r1 = Rectangle(10, 10, 10, 10)
        test1 = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(r1.__str__(), test1)

        r1.update(89)
        test1 = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(r1.__str__(), test1)

        r1.update(89, 2)
        test1 = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(r1.__str__(), test1)

        r1.update(89, 2, 3)
        test1 = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(r1.__str__(), test1)

        r1.update(89, 2, 3, 4)
        test1 = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(r1.__str__(), test1)

        r1.update(89, 2, 3, 4, 5)
        test1 = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(r1.__str__(), test1)

    # Task 9. Update #1
    def test_update_1(self):
        """Correct Output"""
        r1 = Rectangle(10, 10, 10, 10)
        test1 = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(r1.__str__(), test1)

        r1.update(height=1)
        test1 = '[Rectangle] (1) 10/10 - 10/1'
        self.assertEqual(r1.__str__(), test1)

        r1.update(width=1, x=2)
        test1 = '[Rectangle] (1) 2/10 - 1/1'
        self.assertEqual(r1.__str__(), test1)

        r1.update(y=1, width=2, x=3, id=89)
        test1 = '[Rectangle] (89) 3/1 - 2/1'
        self.assertEqual(r1.__str__(), test1)

        r1.update(x=1, height=2, y=3, width=4)
        test1 = '[Rectangle] (89) 1/3 - 4/2'
        self.assertEqual(r1.__str__(), test1)

    # Task 13. Rectangle instance to dictionary representation
    def test_to_dict(self):
        """Correct Output"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        test1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, test1)
        self.assertIsInstance(r1_dictionary, dict)

        r2 = Rectangle(1, 1)
        self.assertNotEqual(r1.__str__(), r2.__str__())
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        test2 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r2_dictionary, test2)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertIsNot(r1.__str__(), r2.__str__())
