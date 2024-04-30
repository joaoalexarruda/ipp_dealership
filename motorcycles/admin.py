from django.contrib import admin

from motorcycles.models import Motorcycle, MotorcycleManufacturer, MotorcycleType

# Register your models here.


class MotorcycleManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class MotorcycleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'engine_size',
                    'motorcycle_type', 'production_year')
    
    search_fields = ('manufacturer', 'model', 'engine_size',
                     'motorcycle_type', 'production_year')
    
    ordering = ('manufacturer', 'model', 'engine_size',
                'motorcycle_type', 'production_year')


admin.site.register(MotorcycleManufacturer, MotorcycleManufacturerAdmin)
admin.site.register(MotorcycleType, MotorcycleTypeAdmin)
admin.site.register(Motorcycle, MotorcycleAdmin)
