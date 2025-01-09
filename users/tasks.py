import datetime

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from config.settings import TG_TOKEN_TO_ACCESS_API

import telebot

telebot.apihelper.ENABLE_MIDDLEWARE = True


def send_message_to_Telegram(current_habits):

    bot = telebot.TeleBot(TG_TOKEN_TO_ACCESS_API)

    for habit in current_habits:
        print(habit.user.tg)
        message = (f"Вам нужно сегодня выполнить привычку '{habit}' "
                   f"в '{habit.time}'")
        bot.send_message(habit.user.tg, message)


@shared_task
def send_message_for_users():
    """
    Собирает все привычки, которые нужно выполнить сегодня.
    И запускает отправку напоминаний о них в Телеграм.
    """
    current_habits = []
    habits = Habit.objects.filter(is_pleasant_habit=False)

    today_date = timezone.datetime.today().date()

    for habit in habits:

        # message = f'{habit.last_date_of_execution}'

        if not habit.last_date_of_execution:
            is_current_habit = True
            # message += ' - new task executed first time'
        else:
            if not habit.period:
                # message += ' - period_days not filled'
                is_current_habit = False
            else:
                next_execution_date = (habit.last_date_of_execution +
                                       datetime.timedelta(days=habit.period)
                                       )
                is_current_habit = next_execution_date == today_date
                # True, False

        if is_current_habit:
            if habit.user.tg == 1:
                print(f"Пользователь {habit.user} не заполнил Telegram ID")
            else:
                habit.last_date_of_execution = today_date
                habit.save()
                current_habits.append(habit)
    print(len(current_habits))

    send_message_to_Telegram(current_habits)

    print("Reminder done")
