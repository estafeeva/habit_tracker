from django.core.management import BaseCommand

from habits.models import Habit
from users.tasks import send_message_to_Telegram


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        i = 0
        if i == 0:
            habits = [item for item in Habit.objects.all()]
            send_message_to_Telegram(habits)
            i +=1
            print(i)
        else:
            pass