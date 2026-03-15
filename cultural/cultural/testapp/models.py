from django.db import models

class Yoga(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Meditation(models.Model):
    title = models.CharField(max_length=100)
    technique = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Festival(models.Model):
    name = models.CharField(max_length=100)
    significance = models.TextField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.name