from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    homeworld = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField()

    def __str__(self):
        return self.name

class Starship(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
