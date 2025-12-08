from django.db import models

class LiveShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='shows/')  # Correct upload path
    is_current = models.BooleanField(default=False)
    preview_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class Shows(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='shows/')
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.title    