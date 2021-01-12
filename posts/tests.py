from django.test import TestCase
from .models import Post, Comment, Category, Author

class AuthorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.zephon= Author(first_name = 'Zephon', last_name ='Makale', email ='mzephon@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.zephon, Author))

class PostTestClass(TestCase):
    def setUp(self):
        # Creating a new post and saving it
        self.zephon= Post(first_name = 'Zephon', last_name ='Makale', email ='mzephon@gmail.com')
        self.zephon.save_post()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.zephon= Category(first_name = 'Zephon', last_name ='Makale', email ='mzephon@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.zephon, Author))
