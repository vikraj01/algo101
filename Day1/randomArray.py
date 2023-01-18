import random
import time
def createRandomArray(num, start = 1, end = 100):
    arr = []
    tmp = random.randint(start, end)
      
    for x in range(num):
          
        while tmp in arr:
            tmp = random.randint(start, end)
              
        arr.append(tmp)
          
      
    return arr

def mili():
        return int(round(time.time() * 1000))