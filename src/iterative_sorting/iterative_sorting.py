# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # save the index of the smallest element found in the array
        smallest_index = cur_index
        print(
            f'\nNew i-Loop started:\nArray: {arr}\ncur_index: {cur_index}\nsmallest_index: {smallest_index}\n')
        # find the smallest element in the array right from the current index (i)
        for j in range(cur_index, len(arr)):
            # if you find an elemet with lower value than the one at smallest_index, update smallest_index value
            if arr[j] < arr[smallest_index]:
                print(
                    f'--- Changing smallest_index from index: {smallest_index} to {j} ---')
                smallest_index = j
        # Swap the element at current index with the element at the smallest index
        print(f'Swapping: {arr[cur_index]} with {arr[smallest_index]}')
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

        print(f'Array after this loop: {arr}')
    return arr


# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    go = True
    while go:
        # reset swaps on every while iteration
        swap = 0
        print(f'\nNew While loop iteration:\nCurrent array: {arr}\n')
        # Loop through the array - 1 (last element can't be looped as it doesnt have [i+1] index)
        for i in range(0, len(arr)-1):
            # Compare each element to its neighbor on the right
            print(f'Comparing i value: {arr[i]} with i+1 value: {arr[i+1]}')
            if arr[i] > arr[i + 1]:
                # If elements in wrong position (relative to each other, swap them)
                print(
                    f'Found wrong position.\nSwapping: {arr[i]} with {arr[i+1]}')
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swap = 1
        # If no swaps performed, stop.
        if swap == 0:
            print(f'\nNo swaps this round. Stopping the While loop. Sorting complete.')
            go = False

        # Else, go back to the element at index 0 and repeat step 1.
    return arr


print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
