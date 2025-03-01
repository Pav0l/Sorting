# STRETCH: implement Linear Search
def linear_search(arr, target):
    res = False
    for i in arr:
        if arr[i] == target:
            res = i

    if not res:
        print('Linear Search: Target not found!')
    else:
        print(f'Linear Search: Found the target value at index {res}')


# linear_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    # check value at mid_idx vs. target value
    # if equal => return mid_idx and end
    # if val[mid_idx] < target => cut out left side from mid_idx and repeat
    # if val[mid_idx] > target => cut out right side from mid_idx and repeat

    low = 0
    high = len(arr)-1
    while low <= high:
        print('\n***New while loop***')

        middle_idx = (high + low) // 2
        print(
            f'list of {arr[low:high]}:\nlow: {low}\nhigh: {high}\nmid_idx: {middle_idx}\ntarget: {target}')

        if target < arr[middle_idx]:
            high = middle_idx - 1
            print(
                f'\nRemoved RHS. New values: \nlow: {low}\nhigh: {high}')
        elif target > arr[middle_idx]:
            low = middle_idx + 1
            print(
                f'\nRemoved LHS. New values: \nlow: {low}\nhigh: {high}')
        else:
            return f'\nTarget found at index: {middle_idx}'
    return '\nTarget not found'


# print(binary_search([0, 1, 2, 3, 4, 5, 6, 8, 9], 7))

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return 'Can not serach in empty list'
    # TO-DO: add missing if/else statements, recursive calls
    print(
        f'\nSearching in arr: {arr[low:high]}\nTarget: {target}\nMid point: {arr[middle]} at index {middle}')
    if target < arr[middle]:
        print(
            f'Target lower than mid. Removing RHS. Resulting arr: {arr[0:middle-1]}')
        return binary_search_recursive(arr, target, 0, middle-1)
    elif target > arr[middle]:
        print(
            f'Target higher than mid. Removing LHS. Resulting arr: {arr[middle+1:high]}')
        return binary_search_recursive(arr, target, middle+1, high)
    elif target == arr[middle]:
        return middle
    else:
        return 'Target not found'

    return f'Target found at index: {middle}'


a = [0, 1, 2, 3, 4, 5, 6, 8, 9]
low = 0
high = len(a)-1
print(binary_search_recursive(a, 8, low, high))
