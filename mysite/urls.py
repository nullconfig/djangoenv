from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers
from api import views
from blogging.feeds import LatestEntriesFeed
from django.urls import reverse

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls),
    path('', include('blogging.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('latest/feed/', LatestEntriesFeed())
]


