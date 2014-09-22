from django.conf.urls import include, patterns, url
from rest_framework import routers
from leaderboards import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users?', views.UserViewSet)
router.register(r'games?', views.GameViewSet)
router.register(r'speedruns?', views.SpeedrunViewSet)
router.register(r'platforms?', views.PlatformViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
