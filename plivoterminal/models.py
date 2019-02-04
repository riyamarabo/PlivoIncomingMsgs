from django.db import models

class Incoming(models.Model):
    phone_number = models.CharField(max_length=11)
    date_time = models.CharField(max_length=100)
    contents = models.TextField()
    def __str__(self):
        return self.phone_number

