from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, about
class TestUrls(SimpleTestCase):

    def test_about_url(self):
        url = reverse('about') #about is from url
        self.assertEquals(resolve(url).func , about) #about is from views
