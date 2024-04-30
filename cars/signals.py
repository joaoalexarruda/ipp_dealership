from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Car, CarBrand, CarInventory


def car_inventory_update():
    """Function to update the car inventory.
    To keep track of the total number of cars in the inventory.
    """
    car_count = Car.objects.all().count()
    CarInventory.objects.create(car_count=car_count)


@receiver(pre_save, sender=CarBrand)
def brand_pre_save(sender, instance, **kwargs):
    instance.name = instance.name.upper()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    instance.model = instance.model.upper()
    instance.color = instance.color.capitalize()
    if not instance.description:
        instance.description = 'No description available'


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, created, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
