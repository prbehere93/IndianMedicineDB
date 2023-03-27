import requests
import queue
import django

django.setup()

from drugs.models import Drug

drug_names = Drug.objects.all().values_list('name', flat=True)

def do_processing(i):
        poke_request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i+1}')
        result = f"{drug_names[i]}.__.{poke_request.json().get('name',0)}"
        return result

def process_consumer(task_queue, results_queue):
        while True:
            try:
                col_number = task_queue.get_nowait()
                result = do_processing(col_number)
                results_queue.put((col_number, result))
                print(f"{col_number}")
            except queue.Empty:
                print('No more columns left to process. Exiting...')
                return
            

# for some reason the ProcessPoolExecutor does not work well with the process_consumer function above
# my guess is that it is 
def worker(col_number):
    while True:
        try:
            print(col_number)
            result = do_processing(col_number)    
            return (col_number, result)
        except queue.Empty:
            print('No more columns left to process. Exiting...')
            return

