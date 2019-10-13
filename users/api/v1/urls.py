from django.conf.urls import url

from .views import UserActiveInactiveView

urlpatterns = [

    url(r'user/(?P<pk>\d+)/active$', UserActiveInactiveView.as_view()),

]