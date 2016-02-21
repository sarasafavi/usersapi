from django.db import models


class ApiGroup(models.Model):
    """Model representing API Groups (not to confused with Django-admin
    groups)"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=12, unique=True)


class ApiUser(models.Model):
    """Model representing API Users (not to confused with Django-admin
    users)"""

    def __str__(self):
        return self.userid

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    userid = models.CharField(max_length=12, unique=True)
    groups = models.ManyToManyField("ApiGroup", related_name="users")
