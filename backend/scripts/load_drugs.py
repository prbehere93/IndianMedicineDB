import csv
from drugs.models import DataSource, Drug, DrugComposition, Manufacturer, DrugType, PackSizeLabel
from pathlib import Path

def run():
    
    try:
        enc = 'utf-8-sig' #had to save_as the original file to a utf-8 compliant file
        file_path=Path.cwd().parent.joinpath('drugs(batch1).csv')
        file_handler=open(file_path, encoding=enc)
        reader=csv.reader(file_handler)
        
        for row in reader:
            
            manufacturer_name,created = Manufacturer.objects.get_or_create(name=row[2])
            drug_type,created =  DrugType.objects.get_or_create(type_of_drug=row[3])
            pack_size_label,created = PackSizeLabel.objects.get_or_create(label=row[4])
            short_composition,created = DrugComposition.objects.get_or_create(short_composition=row[7])
            
            data_source,created=DataSource.objects.get_or_create(name='internal',
                                                                 url='https://www.1mg.com/drugs-all-medicines')
            
            drug, created = Drug.objects.get_or_create(sku_id=row[0],
                                                     name=row[1],
                                                     manufacturer_name=manufacturer_name,
                                                     drug_type=drug_type,
                                                     pack_size_label=pack_size_label,
                                                     price=round(float(row[5]),2),
                                                     rx_required=True if row[6] else False,
                                                     short_composition=short_composition,
                                                     is_discontinued=True if row[8]=="TRUE" else False,
                                                     data_source=data_source
                                                     )
            print(f'{str(drug)}, was {created}')
    except Exception as e:
        print(f'Unable to load the data due to {e}')