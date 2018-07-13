from django.db import models

# Create your models here.
class Song(models.Model):
   title  = models.CharField(max_length=100)
   album  = models.CharField(max_length=60)
   year   = models.IntegerField(blank=True, null=True)
   lyrics = models.TextField(default="Shitty Lyrics")
