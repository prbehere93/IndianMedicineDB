from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract model which provides each model with a created and modified field
    """
    created_on=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Manufacturer(TimeStampedModel):
    name = models.CharField(verbose_name='Manufacturer Name', max_length=100, unique=True)

    def __str__(self):
        return self.name

class DrugComposition(TimeStampedModel):
    short_composition = models.CharField(max_length=600, unique=True)

    def __str__(self):
        return self.short_composition

class PackSizeLabel(TimeStampedModel):
    label = models.CharField(max_length=100, default='', unique=True)

    def __str__(self):
        return self.label

class DataSource(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    source_url = models.URLField(null=True, blank=True) #how to show that the datasource was entered by a user?
    
    def __str__(self):
        return self.name

class DrugType(TimeStampedModel):
    type_of_drug = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.type_of_drug

class Drug(TimeStampedModel):
    sku_id = models.IntegerField(verbose_name='SKU ID', primary_key=True, db_index=True)
    name = models.CharField(verbose_name='Drug Name', max_length=200, db_index=True)
    manufacturer_name = models.ForeignKey(to=Manufacturer, on_delete=models.PROTECT, related_name='manufacturer')
    drug_type = models.ForeignKey(to=DrugType, on_delete=models.PROTECT, related_name='drug_type')
    pack_size_label = models.ForeignKey(to=PackSizeLabel, on_delete=models.PROTECT, related_name='packsize')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    rx_required = models.BooleanField(verbose_name='Prescription Required', null=True)
    short_composition = models.ForeignKey(to=DrugComposition, on_delete=models.PROTECT, related_name='composition')
    is_discontinued = models.BooleanField()
    data_source = models.ForeignKey(to = DataSource, on_delete=models.PROTECT, related_name='source')

    def __str__(self):
        return f'{self.data_source}-{self.sku_id}-{self.name}-{self.manufacturer_name}'

