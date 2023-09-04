from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Insight(models.Model):
    title = models.CharField(max_length=240)
    date = models.DateField(auto_now=True)
    description = models.TextField()
    topic = models.ManyToManyField(Topic, verbose_name="topics")
    section = models.ManyToManyField(Section, verbose_name="sections")
    header_image = models.FileField(upload_to="insight/", max_length=100, null=True)

    def __str__(self) -> str:
        return self.title