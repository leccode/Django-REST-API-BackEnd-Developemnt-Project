from django.db import models

# Here I create the models that data are represented in the DB

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # I create a represented constructor method
    def __str__(self):
        return f"{self.name} is {self.description}"