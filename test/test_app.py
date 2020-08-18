'''Writing unit tests here'''
import unittest
import sys
sys.path.append("..")
import helpers


class TestBlogApp(unittest.TestCase):

    '''
    Class for writing unit test cases
    '''

    def test_initialize_db(self):
        '''
            This method tests whether database file is available or not
        '''
        result = helpers.initialize_db('../data/Database1.json')
        self.assertIsInstance(result, FileNotFoundError)
        print("[test_initialize_db] First test case passed")

        result = helpers.initialize_db("../data/Database.json")
        self.assertIsInstance(result, list)
        print("[test_initialize_db] Second test case passed")

    def test_validate_email(self):
    
        '''
            This method tests email validity
        '''
        result = helpers.validate_email("abc@gmail.com")
        self.assertEqual(result, True)
        print("[test_validate_email] First test case passed")

        result = helpers.validate_email("invalid-email")
        self.assertEqual(result, False)
        print("[test_validate_email] Second test case passed")