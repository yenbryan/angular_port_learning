from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from portfolio.api.views import UserViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'projects', ProjectViewSet, base_name='projects')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rfw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)), # Include router urls into our urlpatterns
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^angular/$', 'portfolio.views.angular', name='angular'),
    url(r'^api-token-auth/', views.obtain_auth_token),
)
