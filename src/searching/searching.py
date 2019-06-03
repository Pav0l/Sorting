# STRETCH: implement Linear Search
def linear_search(arr, target):

    res = 0
    for i in arr:
        if arr[i] == target:
            res = i

    if res != -1:
        print(f'Linear Search: Found the target value at index {res}')
    else:
        print('Linear Search: Target not found!')


linear_search([1, 5, 8, 4, 2, 9, 6, 0, 3, 7], 2)

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    middle = (high + low) // 2

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
