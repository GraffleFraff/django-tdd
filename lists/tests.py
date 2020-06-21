from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    def test_bad_maths(self):
        found = resolve("/")
        self.assertEquals(found.func, home_page)
