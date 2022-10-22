from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tournament(models.Model):
  event_name = models.CharField(max_length=100)
  date = models.DateField()
  game = models.CharField(max_length=100)
  venue = models.CharField(max_length=250)
  prize_pool = models.IntegerField()
  is_complete = models.BooleanField(default=False)
  #links to a user 
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # new code below
  def __str__(self):
      return self.event_name

  def get_absolute_url(self):
    return reverse('user_tournaments_index', kwargs={'user_id': self.user_id})
