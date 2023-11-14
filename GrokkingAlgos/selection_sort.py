def findSmallest(arr):
   smallest = arr[0]
   smallest_index = 0
   for i in range(1, len(arr)):
       if arr[i] < smallest:
           smallest = arr[i]
           smallest_index = i
   return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

# Find the index of minimum element in list

# Using min()
def find_min_index(arr):
    min_value = min(arr)
    min_index = arr.index(min_value)
    return min_index

# Using enumerate()
def find_min_index(arr):
    min_value = min(arr)
    for index, value in enumerate(arr):
        if value == min_value:
            return index

# Using numpy.argmin()
import numpy as np
def find_min_index(arr):
    arr_new = np.array(arr)
    min_index = np.argmin(arr_new)
    return min_index

# Using min() with lambda
def find_min_index(arr):
    min_index = min(range(len(arr)), key=lambda i: arr[i])
    return min_index

# Using sorted()
def find_min_index(arr):
    sorted_pairs = sorted(enumerate(arr), key=lambda x: x[1])
    min_index = sorted_pairs[0][0]
    return min_index

if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))

    my_list = [50, 2, 19, 11, 27]
    min_index = find_min_index(my_list)
    print(" The minimum index position:\n", min_index)