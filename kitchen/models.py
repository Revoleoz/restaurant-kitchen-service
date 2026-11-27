from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", args=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cooks")

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", args=[str(self.id)])

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} (price: {self.price}), dish type: {self.dish_type}"
