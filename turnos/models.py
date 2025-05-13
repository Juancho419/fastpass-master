from django.db import models

class Turno(models.Model):
    hora = models.CharField(max_length=10)
    disponibles = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.hora} ({self.disponibles} disponibles)"
