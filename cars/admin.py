from django.contrib import admin
from cars.models import Car, CarBrand, CarType


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "car_type", "production_year")
    search_fields = ("brand", "model", "car_type", "production_year")
    ordering = ("brand", "model", "car_type", "production_year")


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
