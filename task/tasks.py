from celery import shared_task
from celery.schedules import crontab
from datetime import datetime


@shared_task
def horario(hora):
    print("->>>>> Horário: ", datetime.now())


def teste():
    print("-----------------------")
