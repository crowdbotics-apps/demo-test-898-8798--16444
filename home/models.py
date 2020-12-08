from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Payment(models.Model):
    "Generated Model"
    email = models.EmailField(
        max_length=254,
    )
    card_number = models.CharField(
        max_length=16,
    )
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    cvv = models.CharField(
        max_length=4,
    )
    name = models.CharField(
        max_length=50,
    )
    address = models.TextField()
    city = models.CharField(
        max_length=50,
    )
    state = models.CharField(
        max_length=50,
    )
    zip = models.CharField(
        max_length=10,
    )
    country = models.CharField(
        max_length=50,
    )
