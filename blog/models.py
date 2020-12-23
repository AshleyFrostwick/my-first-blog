from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # links another model
    title = models.CharField(max_length=200) # defines text with limited characters
    text = models.TextField() # long text without a limit
    created_date = models.DateTimeField(default=timezone.now) # sets time and date
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title