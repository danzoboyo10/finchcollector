from email.policy import default
from statistics import mode
from django.db import models
from datetime import date
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
    )
finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
  ordering = ['-date']
    


	# new code below
def __str__(self):
  return self.name

def get_absolute_url(self):
  return reverse('detail', kwargs={'finch_id': self.id})
