def count(arr):
    if not arr:
        return -1
    return 1 + count(arr[1:])
