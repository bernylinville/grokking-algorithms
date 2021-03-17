def find_max(arr):
    if not arr:
        return -1
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
