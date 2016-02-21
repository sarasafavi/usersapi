from django.conf.urls import url, include
from usersproject.views import json404

urlpatterns = [
    url(r'^api/', include('users.urls')),
]

handler404 = json404
