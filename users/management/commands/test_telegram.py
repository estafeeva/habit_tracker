from django.core.management import BaseCommand

from habits.models import Habit
from users.tasks import send_message_to_Telegram


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        habits = [item for item in Habit.objects.all()]
        send_message_to_Telegram(habits)
