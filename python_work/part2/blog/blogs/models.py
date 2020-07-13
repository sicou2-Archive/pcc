from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """A Blog Post for users to give a title, and write about something."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title