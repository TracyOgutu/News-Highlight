import unittest
from app.model import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abcnews','abc','best news ever','https:abc.org','general','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
