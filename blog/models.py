from django.db import models


class PostModel(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()  # no limitation for maximum length of this field
    # Use the PrimaryKey (pk or id) of 'User' model from 'auth' app, as the ForeignKey of PostModel table:
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datatime_create = models.DateTimeField(auto_now_add=True)  # a fix datetime at the time of post creation
    datetime_modified = models.DateTimeField(auto_now=True)  # a datetime that changes everytime we edit a post
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title


