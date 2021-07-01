import time
def bubble(arr, bardraw, timeTick):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bardraw(arr, ['green' if x == j or x == j+1 else 'red' for x in range(len(arr))] )
                time.sleep(timeTick)
    bardraw(arr, ['green' for x in range(len(arr))])