import time
def func():
    starting_time = time.time()
    s=0
    for i in range(1,101):
        s+=i
    ending_time = time.time()
    return ending_time-starting_time
print(func())
