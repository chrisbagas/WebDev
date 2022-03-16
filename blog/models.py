from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
class Blog(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/blog")
    body = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added']

    def get_survey_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments",blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['-added']

