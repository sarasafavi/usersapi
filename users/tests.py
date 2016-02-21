from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from users.models import ApiUser, ApiGroup


class UserRecordTests(APITestCase):

    def setUp(self):

        self.existing_user = {
            "first_name": "Vincent",
            "last_name": "Adultman",
            "userid": "aman"
        }
        self.new_user = {
            "first_name": "Jane",
            "last_name": "Smith",
            "userid": "jsmith",
            "groups": []
        }
        self.good_user = "aman"
        self.bad_user = "nobody"

        # create a pre-existing user record
        ApiUser.objects.create(**self.existing_user)

    def test_create_user(self):
        """We can create new user records
        """
        url = reverse('userlist')
        response = self.client.post(url, self.new_user, format='json')
        stored_user = ApiUser.objects.get(userid=self.new_user.get("userid"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ApiUser.objects.count(), 2)  # existing + new user
        self.assertEqual(
            stored_user.first_name,
            self.new_user.get("first_name"))

    def test_get_bad_user(self):
        """We 404 when trying to get nonexistent user records
        """
        url = reverse('user', kwargs={"userid": self.bad_user})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bad_user(self):
        """We 404 when trying to update nonexistent user records
        """
        url = reverse('user', kwargs={"userid": self.bad_user})
        response = self.client.put(url, self.new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_bad_user(self):
        """We 404 when trying to delete a nonexistent user record
        """
        url = reverse('user', kwargs={"userid": self.bad_user})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_good_user(self):
        """We can get existing user records
        """
        url = reverse('user', kwargs={"userid": self.good_user})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get("first_name"),
            self.existing_user.get("first_name"))

    def test_update_good_user(self):
        """We can update existing user records
        """
        url = reverse('user', kwargs={"userid": self.good_user})
        response = self.client.put(url, self.new_user, format='json')
        updated_user = ApiUser.objects.get(userid=self.new_user.get("userid"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_user.first_name,
                         self.new_user.get("first_name"))

    def test_delete_good_user(self):
        """We can delete existing user records
        """
        url = reverse('user', kwargs={"userid": self.good_user})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        get_deleted_user = self.client.get(url)
        self.assertEqual(
            get_deleted_user.status_code,
            status.HTTP_404_NOT_FOUND)


class GroupTests(APITestCase):

    def setUp(self):

        self.existing_user = {
            "first_name": "Vincent",
            "last_name": "Adultman",
            "userid": "aman"
        }

        # create a few pre-existing records
        ApiGroup.objects.create(name="existing_group")
        ApiUser.objects.create(**self.existing_user)

        self.new_group = {"name": "new_group"}
        self.good_users = ["aman"]
        self.good_group = "existing_group"
        self.bad_group = "nogroup"
        self.bad_users = ["nobody"]

    def test_create_group(self):
        """We can create new groups
        """

        url = reverse('grouplist')
        response = self.client.post(url, self.new_group, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_group(self):
        """We can't create new groups with the same name as an existing
        group
        """

        url = reverse('grouplist')
        response = self.client.post(url, self.good_group, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_bad_group(self):
        """We 404 when trying to get users for a nonexistent group
        """
        url = reverse('group', kwargs={"groupname": self.bad_group})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bad_group(self):
        """We 404 when trying to update nonexistent groups
        """
        url = reverse('group', kwargs={"groupname": self.bad_group})
        response = self.client.put(url, self.good_users, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_bad_group(self):
        """We 404 when trying to delete a nonexistent group
        """
        url = reverse('group', kwargs={"groupname": self.bad_group})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_good_group(self):
        """We can get an existing group
        """
        url = reverse('group', kwargs={"groupname": self.good_group})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_good_group(self):
        """We can update an existing group with existing users
        """
        url = reverse('group', kwargs={"groupname": self.good_group})
        response = self.client.put(url, self.good_users, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_good_group_with_bad_users(self):
        """We 400 when trying to update an existing group with
        non-existent users
        """
        url = reverse('group', kwargs={"groupname": self.good_group})
        response = self.client.put(url, self.bad_users, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_good_group(self):
        """We can delete an existing group by its name
        """
        url = reverse('group', kwargs={"groupname": self.good_group})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        get_deleted_group = self.client.get(url)
        self.assertEqual(
            get_deleted_group.status_code,
            status.HTTP_404_NOT_FOUND)
