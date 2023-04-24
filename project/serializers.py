import re

from rest_framework import serializers

from store.models import Item, Manufacturer, Category


def check_name(value):
    list_of_signs = ['!', '@', '#', '$', '%', '^', '&', '*']
    for sign in value:
        if sign in list_of_signs:
            raise serializers.ValidationError(f'Поле не должно содержать данные символы {list_of_signs} ')


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, validators=[
        check_name
    ])
    price = serializers.IntegerField()
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.manufacturer = validated_data['manufacturer']
        instance.category = validated_data['category']
        instance.save()
        return instance

    def validate_price(self, value):
        if value < 10 or value > 1000:
            raise serializers.ValidationError('Цена должна быть больше 10 и меньше 1000')
        return value


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50, validators=[
        check_name
    ])
    address = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):

    def validate_name(self, data):
        regex = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
        match = regex.search(data)
        if match:
            raise serializers.ValidationError(f'Поле не должно содержать спец.символы')
        return data

    class Meta:
        model = Category
        fields = "__all__"
