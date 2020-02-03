# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i+1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x
            



        # TO-DO: swap
        swap = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = swap



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(len(arr) -1):
            if arr[i] > arr[i + 1]:
                x = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = x
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    count = [0 for i in range(0, maximum)]
    
    # counts the numbers in the array
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, no negative numbers allowed"
        count[arr[i]] += 1
        
        new_arr = [0 for i in range(0, len(arr))]
        j = 0
        for i in range(0, maximum):
            while count[i] > 0:
                new_arr[j] = i
                count[i] -= 1
                j += 1
    return new_arr