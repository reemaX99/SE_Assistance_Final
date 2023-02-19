from django.test import TestCase

from django.urls import  reverse,resolve



# Create your tests here.
class ViewsTestCase(TestCase):


    def test_url_exists(self):
        response = self.client.get("/blog")
        self.assertEqual(response.status_code, 404)

# Create your tests here.
