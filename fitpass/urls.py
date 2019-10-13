"""fitpass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dashboard.views import DashBoardView
from users.views import CustomLoginView, RegisterView, UserProfileView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', login_required(DashBoardView.as_view()), name='dashboard'),
    url(r'^login/$', CustomLoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^user/(?P<pk>\d+)/edit-profile/$', login_required(UserProfileView.as_view()), name='register'),
    url(r'^api/v1/', include('users.api.v1.urls')),
]
