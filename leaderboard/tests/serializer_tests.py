from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django_dynamic_fixture import N, G

from leaderboards.models import Platform, TagValue, Tag, Filter, Speedrun, Game
from leaderboards.serializers import (
    UserSerializer, PlatformSerializer, TagValueSerializer, TagSerializer, FilterSerializer, SpeedrunSerializer,
    GameSerializer
)


class ModelWriteFlatSerializer(SimpleTestCase):
    def test_from_native(self):
        """
        TODO:
        """
        pass

    def test_field_from_native(self):
        """
        TODO:
        """
        pass


class UserSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a User object
        """
        user = N(User, id=1, username='testuser')

        self.assertEqual(UserSerializer(user).data, {
            'id': 1,
            'username': 'testuser',
        })


class PlatformSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a Platform object
        """
        platform = N(Platform, id=1, name='NES')

        self.assertEqual(PlatformSerializer(platform).data, {
            'id': 1,
            'name': 'NES',
        })


class TagValueSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a TagValue object
        """
        tag = G(Tag)
        tag_value = N(TagValue, id=1, name='Any%', description='desc', tag=tag)

        self.assertEqual(TagValueSerializer(tag_value).data, {
            'id': 1,
            'name': 'Any%',
            'description': 'desc',
            'tag': tag.id,
        })


class TagSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a Tag object
        """
        tag = N(Tag, id=1, name='Language', type='type', timed=True)

        self.assertEqual(TagSerializer(tag).data, {
            'id': 1,
            'name': 'Language',
            'type': 'type',
            'timed': True,
            'tagvalues': [],
        })


class FilterSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a Filter object
        """
        filter = N(Filter, id=1, name='Any%')

        self.assertEqual(FilterSerializer(filter).data, {
            'id': 1,
            'name': 'Any%',
            'tagvalues': [],
        })


class SpeedrunSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a Speedrun object
        """
        user = G(User, id=1, username='testuser')
        platform = G(Platform)
        game = G(Game, abbreviation='a')
        speedrun = N(Speedrun, id=1, user=user, time=30, platform=platform, video='url', comments='comments', game=game)

        self.assertEqual(SpeedrunSerializer(speedrun).data, {
            'id': 1,
            'user': {
                'id': 1,
                'username': 'testuser',
            },
            'time': 30,
            'platform': platform.id,
            'video': 'url',
            'comments': 'comments',
            'tagvalues': [],
            'game': game.pk,
        })


class GameSerializerTest(SimpleTestCase):
    def test_serializer(self):
        """
        Should serialize a Game object
        """
        game = N(Game, abbreviation='a', name='test game')

        self.assertEqual(GameSerializer(game).data, {
            'abbreviation': 'a',
            'name': 'test game',
            'tags': [],
            'tagvalues': [],
            'platforms': [],
            'filters': [],
            'speedruns': [],
        })
