def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        left = [x for x in arr if x < arr[0]]
        right = [x for x in arr if x > arr[0]]
        return quicksort(left) +  [arr[0]] +  quicksort(right)


print(quicksort([4,5,3,7,2]))
