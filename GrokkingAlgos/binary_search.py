def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:  # search left part
            high = mid - 1
        else:   # search right part
            low = mid + 1

    return None

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]

    print(binary_search(my_list, 3)) # => 1
    print(binary_search(my_list, -1)) # => None