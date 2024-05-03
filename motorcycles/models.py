from django.db import models

FUEL_CHOICES = [
    ('G', 'Gasoline'),
    ('F', 'Flex Fuel'),
    ('A', 'Alcohol'),
    ('D', 'Diesel'),
    ('H', 'Hybrid'),
    ('E', 'Electric'),
]


class MotorcycleManufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            blank=False, null=False)

    def __str__(self):
        return self.name


class MotorcycleType(models.Model):
    BIKE_TYPES = ('Sport', 'Touring', 'Cruiser', 'Naked', 'Street', 'Electric',
                  'Adventure', 'Scooter', 'Custom', 'Classic', 'Dirt', 'Other')
    name = models.CharField(max_length=50, choices=[
                            (x, x) for x in BIKE_TYPES],)

    def __str__(self):
        return self.name


class Motorcycle(models.Model):
    manufacturer = models.ForeignKey(
        MotorcycleManufacturer, on_delete=models.PROTECT, related_name='motorcycle_manufacturer')
    model = models.CharField(max_length=80, blank=False, null=False)
    engine_size = models.IntegerField(blank=True, null=True)
    motorcycle_type = models.ForeignKey(
        MotorcycleType, on_delete=models.PROTECT, related_name='motorcycle_type')
    production_year = models.IntegerField(blank=False, null=False)
    model_year = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=False, null=False)
    kilometrage = models.IntegerField(blank=True, null=True)
    fuel = models.CharField(
        max_length=1, choices=FUEL_CHOICES, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    image = models.ImageField(
        upload_to='motorcycle_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.manufacturer} {self.model} {self.engine_size} {self.model_year}'


class MotorcycleInventory(models.Model):
    motorcycle_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.motorcycle_count} {self.created_at}'
