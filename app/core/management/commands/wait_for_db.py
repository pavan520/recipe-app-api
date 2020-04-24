import time
from django.db import connections
from django.db import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    "Django command to pause execution untill the db is available"

    def handle(self,*args,**options):
        self.stdout.write('Waiting for db...')
        db_con = None
        while not  db_con:
            try:
                db_con = connections['default']
            except OperationalError:
                self.stdout.write('db unavailable waiting 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('db available!'))

