import unittest
from app.model import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('abcnews','larry','drones today','drones replacing armies','https:abcnews.com','null','2019-11-18T01:51:09Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
