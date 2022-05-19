from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        db_table = "blogs"
