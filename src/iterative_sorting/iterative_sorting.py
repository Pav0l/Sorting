# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    go = True
    while go:
        swap = 0
        # Loop through the array
        for i in range(0, len(arr)-1):
            # Compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # If elements in wrong position (relative to each other, swap them)
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swap = 1
        # If no swaps performed, stop.
        if swap == 0:
            go = False

        # Else, go back to the element at index 0 and repeat step 1.
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
