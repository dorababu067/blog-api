from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    category = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        db_table = "blogs"
