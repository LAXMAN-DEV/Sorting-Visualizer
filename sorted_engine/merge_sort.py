import time

def merge_sort(arr,bardraw,timetick):
    merge_sort_alg(arr,0, len(arr)-1, bardraw, timetick)


def merge_sort_alg(arr,left,right,bardraw,timetick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(arr, left, middle, bardraw, timetick)
        merge_sort_alg(arr, middle+1, right, bardraw, timetick)
        merge(arr, left, middle, right, bardraw, timetick)

def merge(arr,left,middle,right,bardraw,timetick):

    leftPart = arr[left:middle+1]
    rightPart = arr[middle+1: right+1]

    leftIdx = rightIdx = 0

    for arrIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                arr[arrIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                arr[arrIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            arr[arrIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            arr[arrIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    bardraw(arr, ['green' if x >= left and x <= right else 'red' for x in range(len(arr))])
    time.sleep(timetick)
    bardraw(arr, ['green' for x in range(len(arr))])
