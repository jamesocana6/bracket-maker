from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.user.username

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
      return self.user.username

# Create your models here.
class Tournament(models.Model):
  event_name = models.CharField(max_length=100)
  date = models.DateField()
  game = models.CharField(max_length=100)
  venue = models.CharField(max_length=250)
  max_players = models.IntegerField(
    choices=((2, "2"), (4, "4"), (8, "8"), (16, "16"), (32, "32")),
    default=8,
    )
  
  prize_pool = models.IntegerField()
  is_complete = models.BooleanField(default=False)
  players = models.ManyToManyField(Player)
  #links to a user 
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.event_name} id {self.id}"

  def get_absolute_url(self):
    return reverse('user_tournaments_index', kwargs={'user_id': self.user_id})

#   def get_success_url(self):
#     return reverse('user_tournaments_index', kwargs={'user_id': self.user_id})

