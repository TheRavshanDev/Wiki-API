from django.db import models
from user.models import Author

class Post(models.Model):
    user = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=150)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title