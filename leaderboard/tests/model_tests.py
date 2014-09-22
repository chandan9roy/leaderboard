from django.test import SimpleTestCase
from django_dynamic_fixture import N
from leaderboards.models import Platform, Game, Tag, TagValue


class PlatformTest(SimpleTestCase):

    def test_unicode(self):
        """
        Tests the model's unicode method
        """
        self.assertEqual(u'platform', unicode(N(Platform, name='platform')))


class GameTest(SimpleTestCase):

    def test_unicode(self):
        """
        Tests the model's unicode method
        """
        self.assertEqual(u'test game', unicode(N(Game, name='test game')))


class TagTest(SimpleTestCase):

    def test_unicode(self):
        """
        Tests the model's unicode method
        """
        tag = N(Tag, game=N(Game, name='test game'), name='test tag')
        self.assertEqual('test tag for test game', unicode(tag))


class TagValueTest(SimpleTestCase):

    def test_unicode(self):
        """
        Tests the model's unicode method
        """
        tag_value = N(
            TagValue,
            tag=N(Tag, name='test tag', game=N(Game, name='test game')),
            name='test tag value'
        )
        self.assertEqual('test tag: test tag value (test game)', unicode(tag_value))
