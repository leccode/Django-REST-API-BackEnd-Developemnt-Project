from django.contrib import admin
from .models import Drink

# Shows the changes into DB, adding the class Drink

admin.site.register(Drink)