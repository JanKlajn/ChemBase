from django.db import models


# Create your models here.
from django.db.models import Choices
from django.urls import reverse

from accounts.models import User


class Producer(models.Model):
    name = models.CharField(max_length=64)
    country_of_origin = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('update_producer', args=(self.pk, ))


class Reagent(models.Model):
    reagent_name = models.CharField(max_length=256)
    color = models.CharField(max_length=64)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=256, default=None)
    PHYSICAL_STATE = Choices[
        ('PDR', 'Powder'),
        ('LIQ', 'Liquid'),
        ('OIL', 'Oil'),
        ('SLN', 'Solution'),
    ]
    physical_state = models.CharField(
        max_length=3,
        choices=PHYSICAL_STATE,
        default='PDR'
    )
    net_weight_in_grams = models.DecimalField(max_digits=6, decimal_places=2)
    molar_weight = models.DecimalField(max_digits=7, decimal_places=3)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.reagent_name} | by {self.producer} | {self.comment}'

    def get_absolute_url(self):
        return reverse('update_reagent', args=(self.pk, ))


class Solvent(models.Model):
    solvent_name = models.CharField(max_length=64)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    vessel_volume = models.IntegerField(null=False)
    density = models.DecimalField(max_digits=3, decimal_places=1)
    addition_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.solvent_name} | {self.producer} | {self.comment}.'

    def get_absolute_url(self):
        return reverse('update_solvent', args=(self.pk, ))


class Reaction(models.Model):
    reaction_number = models.SmallAutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    reagent = models.ManyToManyField(Reagent, on_delete=models.CASCADE, through_fields='reagent_name')
    solvent = models.ManyToManyField(Solvent, on_delete=models.CASCADE, through_fields='solvent_name')
    start_date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return f'Reaction No {self.reaction_number} by {self.user}.'

    def get_absolute_url(self):
        return reverse('update_reaction', args=(self.pk, ))

