from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^leaderboard/', include('leaderboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
