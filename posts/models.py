import re
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    body=models.TextField()
    slug=models.SlugField(max_length=15,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    

    def __str__(self) -> str:

        return f'{self.slug}-{self.updated}'


    def get_absolute_url(self):
        return reverse('posts:details',args=(self.id,self.slug))

    def likes_count(self):
        return self.post_vote.count()

    def user_can_like(self,user):
        user_like=user.user_vote.filter(post=self)
        if user_like.exists():
            return True
        return False


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    reply=models.ForeignKey('self',on_delete=models.CASCADE,related_name='reply_comment',blank=True,null=True)
    body=models.TextField(max_length=400)
    is_reply=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)




    def __str__(self)->str:
        return f'{self.user} is commented on {self.body[:30]}'





class Vote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_vote')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_vote')


    def __str__(self) -> str:
        return f'{self.user}liked {self.post.slug}'





        