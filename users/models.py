from django.db import models


class Group(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=12, unique=True)


class User(models.Model):
    def __str__(self):
        return self.userid
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    userid = models.CharField(max_length=12, unique=True)
    groups = models.ManyToManyField("Group", related_name="users")
