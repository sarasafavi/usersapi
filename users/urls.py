from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^users/?$', views.UserList.as_view(), name="userlist"),
    url(r'^users/(?P<userid>.*)$', views.UserById.as_view(), name="user"),
    url(r'^groups/?$', views.GroupList.as_view(), name="grouplist"),
    url(
        r'^groups/(?P<groupname>.*)$',
        views.GroupByName.as_view(),
        name="group"),
]
