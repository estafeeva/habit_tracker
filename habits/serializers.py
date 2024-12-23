from rest_framework import serializers

from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
