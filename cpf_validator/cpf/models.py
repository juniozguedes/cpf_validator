from django.db import models

STATUS_CHOICES = [('ALLOW', 'ALLOW'), ('DENY', 'DENY')]


class Cpf(models.Model):
    number = models.CharField(blank=False, max_length=14, unique=True)
    status = models.CharField(
        blank=False,
        max_length=5,
        choices=STATUS_CHOICES,
        default='DENY',
    )
