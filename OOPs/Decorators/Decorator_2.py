import time as t;

def timerAnyBrew(baseFunc):
    def enhancedFunc(*args):
        start = t.time()
        baseFunc(*args)
        end = t.time()
        print(f"time to complete brewing : {end-start} seconds");
    return enhancedFunc

@timerAnyBrew
def brewTea(teaType, timeToBrew):
    print(f"Starting to brew {teaType} Tea")
    t.sleep(timeToBrew)
    print("Tea is ready")
    
@timerAnyBrew    
def brewCoffee():
    print("Starting to brew Coffee")
    t.sleep(3)
    print("Coffee is ready")
    
brewTea("Green", 2)
brewCoffee()