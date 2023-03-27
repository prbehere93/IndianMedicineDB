from django.http import HttpResponse
import time
import requests
import multiprocessing as mp
from multiprocessing import Process
import concurrent.futures as cf
from concurrent.futures import ProcessPoolExecutor

from drugs.models import Drug
from .async_functions import process_consumer, worker

def data_processing():
    pass
    
def current_datetime(request):
    start_time = time.time()
    
    processed_data = {}
    drug_names = Drug.objects.all().values_list('name', flat=True)
    for i in range(0,155):
        poke = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i+1}')
        processed_data[i+1] = f"{drug_names[i]}.__.{poke.json().get('name',0)}"
        
    end_time = time.time()
    html = f"""<html><body>Time taken to run the script = {end_time - start_time}.</body>
                     <p>Data = {processed_data}.</p>   
                </html>"""
    # Time taken to run the script = 19.143165588378906.
    # Time taken to run the script = 20.036739110946655.
    # Time taken to run the script = 25.14482045173645.
    # Time taken to run the script = 23.803631067276.
    # Time taken to run the script = 29.13687300682068.


    return HttpResponse(html)

def async_current_datetime(request):
    start_time = time.time()
    processed_data = {} # for storing the results
    
    work_to_do = mp.JoinableQueue()
    work_done = mp.SimpleQueue()    
    [work_to_do.put(i) for i in range(0,155)] # adding no. of loops in the task_queue     
    max_workers = 12

    process_pool = [Process(target=process_consumer, args=(work_to_do, work_done)) for _ in range(max_workers)]
    
    [p.start() for p in process_pool] #starting the processes
    [p.join() for p in process_pool]
    [p.close() for p in process_pool] #stopping the process
    
    #fetching the data in a dictionary
    while not work_done.empty():
        col_num, result = work_done.get()
        print(col_num, result)
        processed_data[col_num] = result
        
    
    no_of_objects = len(processed_data)
    end_time = time.time()
    
    html = f"""<html><body>Time taken to run the script = {end_time - start_time}.</body>
                     <p>Data = {processed_data}.</p>
                     <p>No. of objects = {no_of_objects}.</p> 
                </html>"""
    # Time taken to run the script = 20.26284098625183.
    # Time taken to run the script = 17.138067960739136.
    # Time taken to run the script = 7.008494853973389. (increased max_workers to 10)
    # Time taken to run the script = 6.275712966918945.
    # Time taken to run the script = 6.347433567047119.
    # Time taken to run the script = 5.9084460735321045.
    # Time taken to run the script = 6.328838109970093.
    # Time taken to run the script = 6.584982872009277.
    # increased to 12
    # Time taken to run the script = 4.916522741317749.
    # Time taken to run the script = 5.318272590637207.
    # Time taken to run the script = 5.189968585968018.
    # Time taken to run the script = 5.199074029922485.


    return HttpResponse(html)

def ppe_current_datetime(request):
    """
    Using the MultiProcessingPool
    """
    start_time = time.time()
    
    work_to_do = mp.JoinableQueue()
    work_done = mp.SimpleQueue()  
    [work_to_do.put(i) for i in range(0,155)]
    processed_data = {}
    
    # #setting the max_workers to the CPU count
    with ProcessPoolExecutor(max_workers=12) as ex:
        futures = [
            ex.submit(worker, i) for i in range(0,155)
        ]
        
        for future in futures:
            col_num, result = future.result()
            processed_data[col_num] = result
    
    no_of_objects = len(processed_data)    
    end_time = time.time()
    
    html = f"""<html><body>Time taken to run the script = {end_time - start_time}.</body>
                <p>Data = {processed_data}.</p>
                <p>No. of objects = {no_of_objects}.</p> 
            </html>"""
    # Time taken to run the script = 5.768132925033569.
    # Time taken to run the script = 5.763936758041382.
    # Time taken to run the script = 5.3697357177734375.

    return HttpResponse(html)





 


