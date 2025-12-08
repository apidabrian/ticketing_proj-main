from django.db import models

class LiveShows(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
