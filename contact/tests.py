
from django.test import TestCase ,SimpleTestCase
from django.urls import  reverse,resolve

from .views import show_contact

# Create your tests here.
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_url_exists(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/faculty_member.html')