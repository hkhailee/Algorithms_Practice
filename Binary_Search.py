# implementation of basic binary search in Python.
arr = [10, 12, 30, 24, 55, 86, 97, 80, 94, 100]


def binary_search(arr, item):
    arr = sorted(arr) # ensuring arr is sorted
    low = 0 
    high = len(arr) - 1
    # binary searh 'algorithm'
    while low <= high :
        mid = (low + high) // 2 # splitting list arr in half
        guess = arr[mid] # middle value of arr
        if guess == item :
            return guess
        elif guess < item:
            low = mid + 1 
        else :
            high = mid - 1
    return None

print(binary_search(arr, 100))