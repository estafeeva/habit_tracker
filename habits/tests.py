from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User

from django.urls import reverse


class HabitTestCase(APITestCase):
    # Задаем данные для тестов
    def setUp(self):
        self.user = User.objects.create(
            email="admin3@example.com",
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.habit = Habit.objects.create(
            action="Сделать зарядку",
            user=self.user,
            reward="Отдохнуть"
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habit-list")
        data = {
            "action": "test",
            "duration": 20,
            "period": 1,
            "user": self.user.pk,
            "is_pleasant_habit": True
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {"action": "test2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "test2")

    def test_habit_delete(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.habit.pk,
                        'duration': None,
                        'period': None,
                        'place': None,
                        'time': None,
                        'action': self.habit.action,
                        'is_pleasant_habit': False,
                        'reward': self.habit.reward,
                        'is_public': False,
                        'last_date_of_execution': None,
                        'user': self.user.pk,
                        'linked_habit': None
                    }
                ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
