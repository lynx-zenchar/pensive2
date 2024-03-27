from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    author_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)



    def __str__(self):
        return self.title