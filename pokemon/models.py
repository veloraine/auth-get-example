from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pokemon(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    level = models.IntegerField()
    element_type = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name} | {self.user.username}'