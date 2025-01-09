from rest_framework import serializers

from habits.models import Habit
from habits.validators import validate_duration, validate_period, validate_reward_or_pleasant_habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[validate_duration])
    period = serializers.IntegerField(validators=[validate_period])

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        is_pleasant_habit = self.get_actual_field_for_validation(
            attrs,
            "is_pleasant_habit"
        )
        linked_habit = self.get_actual_field_for_validation(
            attrs,
            "linked_habit"
        )
        reward = self.get_actual_field_for_validation(attrs, "reward")

        validate_reward_or_pleasant_habit(is_pleasant_habit, linked_habit, reward)

        return attrs

    def get_actual_field_for_validation(self, data_dict, key):

        instance_habit = self.instance

        if key in data_dict:
            """если в словаре задано новое поле"""
            value = data_dict.get(key)

        elif instance_habit is None:
            """если нет нового поля и ранее не было задано старое поле"""
            value = None

        else:
            """если нет нового поля, но ранее было задано старое поле"""
            value = getattr(instance_habit, key)  # == instance_habit."key"

        return value