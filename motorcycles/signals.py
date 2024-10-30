from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Motorcycle, MotorcycleManufacturer, MotorcycleInventory


def motorcycle_inventory_update():
    """Function to update the motorcycle inventory.
    To keep track of the total number of motorcycles in the inventory.
    """
    motorcycle_count = Motorcycle.objects.all().count()
    MotorcycleInventory.objects.create(motorcycle_count=motorcycle_count)


@receiver(pre_save, sender=MotorcycleManufacturer)
def manufacturer_pre_save(sender, instance, **kwargs):
    instance.name = instance.name.upper()


@receiver(pre_save, sender=Motorcycle)
def motorcycle_pre_save(sender, instance, **kwargs):
    instance.model = instance.model.upper()
    instance.color = instance.color.capitalize()
    if not instance.description:
        instance.description = "No description available"


@receiver(post_save, sender=Motorcycle)
def motorcycle_post_save(sender, instance, created, **kwargs):
    motorcycle_inventory_update()


@receiver(post_delete, sender=Motorcycle)
def motorcycle_post_delete(sender, instance, **kwargs):
    motorcycle_inventory_update()
