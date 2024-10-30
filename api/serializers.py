from rest_framework import serializers
from cars.models import Car
from motorcycles.models import Motorcycle


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                "Description must be at least 20 characters long."
            )
        return value


class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = "__all__"

    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                "Description must be at least 20 characters long."
            )
        return value
