from django.db import models


class Fleet(models.Model):
    deviceid = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.deviceid
