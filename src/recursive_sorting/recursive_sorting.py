
def merge(left, right):
    merged_arr = []
    print(f'\nMerging left: {left} with right: {right}')
    for i in range(len(left) + len(right)):
        if len(left) == 0:
            print(
                f'All elements in LEFT list have been merged. Appending right {right} to the merged_arr: {merged_arr}')
            merged_arr += right
            break
        elif len(right) == 0:
            print(
                f'All elements in RIGHT list have been merged. Appending left {left} to the merged_arr: {merged_arr}')
            merged_arr += left
            break
        elif left[0] > right[0]:
            print(
                f'Merging right element {right[0]} to merged_arr')
            merged_arr.append(right.pop(0))
            print(
                f'Current merged_arr: {merged_arr};\nRemaining right list: {right}\n')
        else:
            print(
                f'Merging left element {left[0]} to merged_arr')
            merged_arr.append(left.pop(0))
            print(
                f'Current merged_arr: {merged_arr};\nRemaining left list: {left}\n')
    print(f'\n****** Returning merged_arr: {merged_arr} ******\n')
    return merged_arr


# implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Divide the array untill it's n elements of len 1
    if len(arr) > 1:
        print(f'\nDivide {arr} into:')
        left = merge_sort(arr[0:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        print(f'left list: {left}\nright list: {right}')

        # Merge sorted pieces together
        arr = merge(left, right)

    return arr


# merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
