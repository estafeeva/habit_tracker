from rest_framework import serializers
from rest_framework.serializers import ValidationError


def validate_reward_or_pleasant_habit(is_pleasant_habit, linked_habit, reward):
    """
    Исключает одновременный выбор связанной привычки и указания вознаграждения.
    В модели не должно быть заполнено одновременно и поле вознаграждения, и
    поле связанной привычки. Можно заполнить только одно из двух полей.
    """
    if is_pleasant_habit == False and reward and linked_habit:
        raise serializers.ValidationError("Вы не можете заполнить одновременно и связанную привычку, и вознаграждение. Выберите что-то одно.")

    if not is_pleasant_habit and not reward and not linked_habit:
        raise serializers.ValidationError("Заполните или связанную привычку, или вознаграждение.")

    """
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """
    if not is_pleasant_habit and linked_habit and linked_habit.is_pleasant_habit==False:
        raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")

    """
    У приятной привычки не может быть вознаграждения или связанной привычки.
    """
    if is_pleasant_habit and (linked_habit or reward):
        raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


def validate_duration(value):
    """Время выполнения должно быть не больше 120 секунд."""
    if value > 120:
        raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")


def validate_period(value):
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""
    if value > 7:
        raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
