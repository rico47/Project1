from django.db import models


class Webpage(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    description = models.TextField()


class Stats(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    idx_js = models.IntegerField()
    idx_html = models.IntegerField()
    idx_image = models.ImageField()
    idx_bool = models.BooleanField()


