def quicksort(arr):
    if len(arr) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return arr

    else:
        # recursive case
        pivot = arr[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
