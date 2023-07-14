from django.db import models


class Stove(models.Model):
    stoves_num = models.IntegerField(default=0)
    date = models.DateField()
    work_num = models.IntegerField()
    work_time = models.FloatField()

    def __str__(self):
        return f'{self.stoves_num, self.date, self.work_num, self.work_time}'