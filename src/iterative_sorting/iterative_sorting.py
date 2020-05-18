# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    while True:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] =  arr[i+1], arr[i]
                swapped = True
        if swapped is False:
            break


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    if len(arr) == 0:
        return arr
    maximum = max(arr)
    count = [0] * (maximum + 1)
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1
    
    j = 0
    for i in range(len(count)):
        while count[i]:
            arr[j] = i
            j += 1
            count[i] -= 1
            # print(count, arr)

    return arr
