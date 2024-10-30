from django.db import models

class DailyMission(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)




    def __str__(self):
        return self.title