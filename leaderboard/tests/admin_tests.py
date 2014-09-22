from django.test import SimpleTestCase

from leaderboards import admin


class AdminTest(SimpleTestCase):
    """
    Tests that the admin can be loaded.
    """
    def test_load_admin(self):
        assert(admin)
