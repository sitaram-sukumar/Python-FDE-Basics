import time as t;

def timerAnyBrew(baseFunc):
    def enhancedFunc():
        start = t.time()
        baseFunc()
        end = t.time()
        print(f"time to complete brewing : {end-start} seconds");
    return enhancedFunc

@timerAnyBrew
def brewTea():
    print("Starting to brew Tea")
    t.sleep(1)
    print("Tea is ready")
    
@timerAnyBrew    
def brewCoffee():
    print("Starting to brew Coffee")
    t.sleep(3)
    print("Coffee is ready")
    
brewTea()
brewCoffee()