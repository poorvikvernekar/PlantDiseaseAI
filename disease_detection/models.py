from django.db import models

class DiseaseInfo(models.Model):

    disease_name = models.CharField(
        max_length=200,
        unique=True
    )

    description = models.TextField()

    signs_of_damage = models.TextField()

    prevention = models.TextField()

    recommendation = models.TextField()   # <-- Add this

    crop_health = models.IntegerField()

    yield_loss = models.IntegerField()

    def __str__(self):
        return self.disease_name