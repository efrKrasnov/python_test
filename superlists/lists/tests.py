from django.urls import resolve
from django.test import TestCase
from django.http import HttpResponse

from lists.views import home_page

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response: HttpResponse = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
