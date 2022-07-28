from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    slug=models.SlugField(max_length=15,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    

    def __str__(self) -> str:

        return f'{self.slug}-{self.updated}'


    def get_absolute_url(self):
        return reverse('posts:details',args=(self.id,self.slug,))





        