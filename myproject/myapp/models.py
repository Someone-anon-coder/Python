from django.db import models

# Define a model for a blog post
class Post(models.Model):
    # The title of the post, limited to 100 characters
    title = models.CharField(max_length=100)
    # The content of the post, can be any length
    content = models.TextField()
    # The date and time the post was published, automatically set when the post is created
    published_date = models.DateTimeField(auto_now_add=True)

    # Return the title of the post as a string representation
    def __str__(self):
        return self.title