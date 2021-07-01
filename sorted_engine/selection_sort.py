import sys
import time
def selection(arr,bardraw, timeTick):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:      
                arr[i], arr[j] = arr[j], arr[i]
                bardraw(arr, ['green' if x == i or x == j else 'red' for x in range(len(arr))] )
                time.sleep(timeTick)
    bardraw(arr, ['green' for x in range(len(arr))])