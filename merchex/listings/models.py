from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
 
    def __str__(self):
            return self.name
class Listings(models.Model):
    class ListingType(models.TextChoices):
        ACCORDS='A',
        CLOTHING='C',
        POSTERS='P',
        RISC='R',
        MUSIC='M'
        
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=255)
    sold=models.fields.BooleanField(default=True,null=True)
    year=models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    type=models.fields.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering=('title',)
        verbose_name_plural='Listings'