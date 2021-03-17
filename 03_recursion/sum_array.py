def sum_array(arr):
    if not arr:
        return -1

    return arr[0] + sum_array(arr[1:])
