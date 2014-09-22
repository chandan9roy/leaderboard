from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from leaderboards.serializers import UserSerializer, GameSerializer, SpeedrunSerializer, PlatformSerializer
from leaderboards.models import Game, Speedrun, Platform
from leaderboards.permissions import IsAuthenticatedOrReadOnly


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    Require authentication when creating; otherwise read-only access.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class SpeedrunViewSet(CreateListRetrieveViewSet):
    """
    API endpoint that allows speedruns to be viewed or edited.
    """
    queryset = Speedrun.objects.all()
    serializer_class = SpeedrunSerializer


class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows platforms to be viewed or edited.
    """
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
