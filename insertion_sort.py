#!/bin/python3
import sys

def insertionSort2(n, arr):
    
    for i in range(2,len(arr)+1):
        num = arr[:i][-1]
        for j in reversed(range(len(arr[:i])-1)):
            if num < arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        
        print(" ".join(str(x) for x in arr))
            
            
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
