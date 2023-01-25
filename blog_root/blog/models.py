from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



category =(
    ("Python", "Python"),
    ("DevOps", "DevOps"),
    ("Linux", "Linux"),
    ("Django", "Django"),
)
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=category)
    title = models.CharField(max_length=150)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



