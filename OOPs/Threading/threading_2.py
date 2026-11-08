import time
import threading

def check_serv(serv_name):
    print("checking for Customer API" )
    time.sleep(2)
    print("Customer API responding" )

thread = threading.Thread(
    target=check_serv,
    args=("Customer API",)
)

thread.start()
#thread.join()

print("monitoring cehck completed" )