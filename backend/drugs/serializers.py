from rest_framework.response import Response
from rest_framework import serializers
from .models import Drug, Manufacturer, PackSizeLabel, DataSource, DrugComposition, DrugType

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('name',)
        extra_kwargs = {
            'name': {'validators': []},
        }

class PackSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackSizeLabel
        fields = ('label',)
        extra_kwargs = {
            'label': {'validators': []},
        }

class DrugTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugType
        fields = ('drug_type',)
        extra_kwargs = {
            'type': {'validators': []},
        }

class DrugCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugComposition
        fields = ('short_composition',)
        extra_kwargs = {
            'short_composition': {'validators': []},
        }

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ('name', 'url')
        extra_kwargs = {
            'name': {'validators': []},
        }

class DrugSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer_name = ManufacturerSerializer()
    drug_type = DrugTypeSerializer()
    pack_size_label = PackSizeSerializer()
    short_composition = DrugCompositionSerializer()
    data_source = DataSourceSerializer()
    
    class Meta:
        fields = ('url', 'sku_id', 'name', 'manufacturer_name', 'drug_type', 
            'pack_size_label', 'price', 'rx_required', 'short_composition',
             'is_discontinued', 'data_source',)
        model = Drug

    def create(self, validated_data):
        manufacturer_data = validated_data.pop('manufacturer_name')
        manufacturer_obj, _ = Manufacturer.objects.get_or_create(**manufacturer_data)

        type_data = validated_data.pop('drug_type')
        type_obj, _ = DrugType.objects.create(**type_data)

        label_data = validated_data.pop('pack_size_label')
        label_obj, _ = PackSizeLabel.objects.get_or_create(**label_data)

        composition_data = validated_data.pop('short_composition')
        composition_obj, _ = DrugComposition.objects.get_or_create(**composition_data)

        data_source_data = validated_data.pop('data_source')
        data_source_obj, _ = DataSource.objects.get_or_create(**data_source_data)

        drug_obj, _ = Drug.objects.get_or_create(manufacturer_name=manufacturer_obj,
                            drug_type=type_obj,
                            pack_size_label=label_obj,
                            short_composition=composition_obj,
                            data_source=data_source_obj,
                            **validated_data)
        return drug_obj
