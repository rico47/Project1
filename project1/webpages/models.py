from django.db import models


class Webpage(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Stats(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    idx_js = models.IntegerField()
    idx_html = models.IntegerField()
    idx_image = models.ImageField(null=True, blank=True)
    idx_bool = models.BooleanField()


