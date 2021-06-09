#!/usr/bin/python3
"""Unittest foralmost a circle / base
"""
import unittest
import os

import models.base
from models.base import Base
from models.rectangle import Rectangle


class Test_Base_Reqeriments(unittest.TestCase):
    """Class to test the base class requeriments"""

    # Testing README file
    def test_readme(self):
        """Test if README file exist and is not empty"""
        readme = os.getcwd()
        readme1 = readme + '/README.md'
        readme2 = os.path.exists(readme1)
        self.assertTrue(readme2, True)

        with open(readme1, 'r') as fd:
            x = fd.read()
            self.assertTrue(len(x) > 0)

    # Testing pep8 and shebang
    def test_pep8_Base(os_system):
        """PEP8 validation"""
        os_system.assertEqual(os.system("pep8 ./models/base.py"), 0)

    def test_pep8_test_base(os_system):
        """PEP8 validation"""
        path = os.system("pep8 tests/test_models/test_base.py")
        os_system.assertEqual(path, 0)

    def test_shebang(self):
        """First line contains #!/usr/bin/python3"""
        with open('./models/base.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    def test_shebang_test_base(self):
        """First line contains #!/usr/bin/python3"""
        with open('./tests/test_models/test_base.py', 'r') as fd:
            x = fd.read()
            line = x.splitlines()
            self.assertEqual(line[0], '#!/usr/bin/python3')

    # Documentation for Module, class and methods exist
    def test_docmodule(self):
        """Module is documented"""
        temp = models.base.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_docclass(self):
        """Class is documented"""
        temp = Base.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_constructor(self):
        """init is documented"""
        temp = Base.__init__.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)

    def test_doc_methods(self):
        """Functions are documented"""
        # to_json_string
        temp = Base.to_json_string.__doc__
        self.assertTrue(temp is not None and len(temp) > 0)


class Test_Base(unittest.TestCase):
    """Class to test the base class code"""

    def setUp(self):
        """setup nb_objectes to 0 after each test"""
        Base._Base__nb_objects = 0

    def test_base_class_constructor(self):
        """testing init functión"""
        self.assertEqual(Base._Base__nb_objects, 0)

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    # Task 15. Dictionary to JSON string
    def test_to_json_string(self):
        """correct aoutput"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        test1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        # test2 = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(dictionary, test1)
        self.assertIsInstance(dictionary, dict)
        # self.assertEqual(json_dictionary, test2)
        self.assertIsInstance(json_dictionary, str)

        # TEST NONE LIST
        json_dictionary = Base.to_json_string(None)
        self.assertIsInstance(json_dictionary, str)
        # TEST EMPTY LIST
        json_dictionary = Base.to_json_string([])
        self.assertIsInstance(json_dictionary, str)

    # Task 16. Dictionary to JSON string
    def test_save_to_file(self):
        """Correct output"""
        new_list = None
        self.assertTrue(type(Base.save_to_file(new_list)), [])

    # Task 17. JSON string to dictionary
    def from_json_string(self):
        """Correct output"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), "list")
        self.assertEqual(type(json_list_input), "str")
        self.assertEqual(type(list_output), "list")
