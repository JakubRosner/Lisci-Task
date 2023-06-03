from core.models import Course, LearningActivity, UserData
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class CourseViewSetCRUDTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.course = Course.objects.create(name="Test Course")

    def test_create_course(self):
        url = reverse("course-list")
        data = {"name": "New Course"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Course.objects.count(), 2)

    def test_retrieve_course(self):
        url = reverse("course-detail", kwargs={"pk": self.course.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Test Course")

    def test_update_course(self):
        url = reverse("course-detail", kwargs={"pk": self.course.pk})
        data = {"name": "Updated Course"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Course.objects.get(pk=self.course.pk).name, "Updated Course")

    def test_delete_course(self):
        url = reverse("course-detail", kwargs={"pk": self.course.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Course.objects.count(), 0)


class LearningActivityViewSetCRUDTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.course = Course.objects.create(name="Test Course")
        self.learning_activity = LearningActivity.objects.create(
            name="Test Activity", course=self.course
        )

    def test_create_learning_activity(self):
        url = reverse("learningactivity-list")
        data = {"name": "New Activity", "course": self.course.pk}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            LearningActivity.objects.count(), 2
        )  # Assuming there's already one learning activity created

    def test_retrieve_learning_activity(self):
        url = reverse(
            "learningactivity-detail", kwargs={"pk": self.learning_activity.pk}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Test Activity")

    def test_update_learning_activity(self):
        url = reverse(
            "learningactivity-detail", kwargs={"pk": self.learning_activity.pk}
        )
        data = {"name": "Updated Activity"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            LearningActivity.objects.get(pk=self.learning_activity.pk).name,
            "Updated Activity",
        )

    def test_delete_learning_activity(self):
        url = reverse(
            "learningactivity-detail", kwargs={"pk": self.learning_activity.pk}
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(LearningActivity.objects.count(), 0)


class UserDataViewSetCRUDTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.course = Course.objects.create(name="Test Course")
        self.learning_activity = LearningActivity.objects.create(
            name="Test Activity", course=self.course
        )
        self.user_data = UserData.objects.create(
            user=self.user,
            learning_activity=self.learning_activity,
            data="Some test data",
            status="In progress",
        )

    def test_create_user_data(self):
        url = reverse("userdata-list")
        data = {
            "user": self.user.pk,
            "learning_activity": self.learning_activity.pk,
            "data": "New test data",
            "status": "COMPLETED",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            UserData.objects.count(), 2
        )  # Assuming there's already one user data created

    def test_retrieve_user_data(self):
        url = reverse("userdata-detail", kwargs={"pk": self.user_data.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"], "Some test data")

    def test_update_user_data(self):
        url = reverse("userdata-detail", kwargs={"pk": self.user_data.pk})
        data = {"status": "COMPLETED"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserData.objects.get(pk=self.user_data.pk).status, "COMPLETED")

    def test_delete_user_data(self):
        url = reverse("userdata-detail", kwargs={"pk": self.user_data.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(UserData.objects.count(), 0)


class UserViewSetCRUDTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_create_user(self):
        url = reverse("user-list")
        data = {"username": "testuser2", "password": "1234StrongPassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 2)

    def test_retrieve_user(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser")

    def test_update_user(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        data = {"first_name": "Doni"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(pk=self.user.pk).first_name, "Doni")

    def test_delete_user(self):
        url = reverse("user-detail", kwargs={"pk": self.user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(User.objects.count(), 0)
