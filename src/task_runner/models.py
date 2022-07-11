import logging

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .services.task import fake_task_runner as task_runner


class Task(models.Model):
    input = models.IntegerField(validators=[MinValueValidator(100000), MaxValueValidator(99999999)])

    result = models.CharField(max_length=256, default='')

    def __str__(self):
        return f"{self.input}: - ({'processing' if (self.result == '') else self.result})"

    def save(self, *args, **kwargs):
        if self.result == '':
            try:
                self.result = task_runner(self.input)
            except Exception as e:
                self.result = str(e)
                logging.exception(e)

        super().save(*args, **kwargs)

