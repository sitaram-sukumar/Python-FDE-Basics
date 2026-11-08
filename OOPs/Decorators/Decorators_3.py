import time as t;

def timerAnyBrew(baseFunc):
    def enhancedFunc(*args, **kwargs):
        start = t.time()
        baseFunc(*args, **kwargs)
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
    
brewTea(teaType="Green", timeToBrew=1)
brewCoffee()
