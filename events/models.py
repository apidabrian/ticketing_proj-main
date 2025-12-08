from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')  # Correct upload path
    is_current = models.BooleanField(default=False)
    preview_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title