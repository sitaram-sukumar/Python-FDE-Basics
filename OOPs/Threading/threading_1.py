# we are building a company monitoring service
# A customer DB 
# external weather API
# an AI inference service

import time

def readCustomer():
    print("Reading cusotmer record...")
    time.sleep(2)
    print("cusotmer record received...")
    
    
def FetchWeather():
    print("Reading weather record...")
    time.sleep(3)
    print("cusotmer weather received...")   
    
def run_prediction():
    print("Reading AI Inference record...")
    time.sleep(2)
    print("cusotmer AI Inference received...")
    
start = time.perf_counter()    
readCustomer()
FetchWeather()
run_prediction()

end = time.perf_counter()    
print(f"Tiotal Time : {end-start:.2f} seconds")