from django.db import models


class Blog(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_body = models.TextField()
    date = models.DateField()
    blog_url = models.URLField(blank=True)

    def __str__(self):
        return self.blog_title

