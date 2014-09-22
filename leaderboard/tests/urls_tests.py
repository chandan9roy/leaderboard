from django.test import SimpleTestCase

from leaderboards.urls import urlpatterns


class UrlsTest(SimpleTestCase):
    def test_that_urls_are_defined(self):
        """
        Should have several urls defined.
        """
        self.assertTrue(len(urlpatterns) > 0)
