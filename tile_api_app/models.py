from django.db import models

# Create your models here.

class Tile(models.Model):
    
    class Status(models.TextChoices):
        LIVE = 'live', 'Live'
        PENDING = 'pending', 'Pending'
        ARCHIVED = 'archived', 'Archived'

    launch_date = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)


class Task(models.Model):

    class Type(models.TextChoices):
        SURVEY = 'survey', 'Survey'
        DISCUSSION = 'discussion', 'Discussion'
        DIARY = 'diary', 'Diary'

    title = models.CharField(max_length=255)
    order = models.IntegerField() # The spec is unclear on the use case for this field so it may need refactoring
    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.SURVEY)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)



