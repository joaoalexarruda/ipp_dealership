from django.db import models


TRANSMISSION_CHOICES = [
    ('M', 'Manual'),
    ('A', 'Automatic'),
]

FUEL_CHOICES = [
    ('G', 'Gasoline'),
    ('F', 'Flex Fuel'),
    ('A', 'Alcohol'),
    ('D', 'Diesel'),
    ('H', 'Hybrid'),
    ('E', 'Electric'),
]


class CarBrand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarType(models.Model):
    CAR_TYPES = ('Sedan', 'SUV', 'Hatchback', 'Coupe', 'Convertible', 'Wagon',
                 'Van', 'Pickup', 'Truck', 'Electric', 'Hybrid', 'Other')
    name = models.CharField(max_length=50, choices=[
                            (x, x) for x in CAR_TYPES],)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(
        CarBrand, on_delete=models.PROTECT, related_name='car_brand')
    model = models.CharField(max_length=100)
    production_year = models.IntegerField(blank=False, null=False)
    model_year = models.IntegerField(blank=True, null=True)
    car_type = models.ForeignKey(
        CarType, on_delete=models.PROTECT, related_name='car_type')
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=50, blank=False, null=False)
    power = models.IntegerField(blank=True, null=True)
    fuel = models.CharField(max_length=1, choices=FUEL_CHOICES)
    doors = models.IntegerField(blank=True, null=True)
    kilometrage = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    image = models.ImageField(
        upload_to='car_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.production_year}'


class CarInventory(models.Model):
    car_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.car_count} {self.created_at}'
