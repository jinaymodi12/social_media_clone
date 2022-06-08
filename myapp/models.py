from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    CHOICE = (
      ('Male','Male'),
       ('Female','Female'),
    )
    name = models.CharField(max_length=10)
    gender = models.CharField(choices=CHOICE,max_length=6)
    mobile = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=50)
    profile = models.FileField(upload_to='profile',null=True,blank=True)
    followers = models.ManyToManyField('User',related_name='follower')
    following = models.ManyToManyField('User',related_name='followings')

    @property
    def folowing_count(self):
      self.following.all.count()

    @property
    def followers_count(self):
      self.followers.all.count()
  
class AddPost(models.Model):
 user = models.ForeignKey(User,on_delete=models.CASCADE)
 post_date = models.DateField(auto_now_add=True)
 post = models.FileField(upload_to='post')
 like =  models.ManyToManyField('User',related_name='lik')
 description = models.CharField(max_length=50,null=True,blank=True)

 @property
 def post_count(self):
      self.post.count
 
class Comment(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   add_post = models.ForeignKey(AddPost,on_delete=models.CASCADE)
   date = models.DateField(auto_now_add=True)
   comment = models.TextField(max_length=250)




   