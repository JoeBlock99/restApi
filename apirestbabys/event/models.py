from django.db import models
import datetime 

class Event(models.Model):
    head = models.CharField(max_length=50, null=True, blank=False)
    body = models.CharField(max_length=200)
    date = datetime.datetime.now()
    baby = models.ForeignKey(
        'baby.Baby',
        related_name='events',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}, \n {}: \n {}\n {}'.\
            format(self.baby.name, self.head, self.body, self.date)
