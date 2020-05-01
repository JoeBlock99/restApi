from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=30, null=True)
    parent = models.ForeignKey(
        'parent.Parent',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Hello {} your child {}'.format(self.parent.name, self.name)
