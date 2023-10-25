# Remove Element

# --------------- Method 1 -----------------
# Using a support list and a support variable
# Time: O(n)
# Space: O(n), where n = len(nums)

def removeElement(nums: list[int], val: int) -> int:
    k = 0
    res = []
    for i in range(len(nums)):
        if nums[i] != val:
            res.append(nums[i])
            k += 1
        nums[i] = 0
    
    for i in range(len(res)): # copy res to nums
        nums[i] = res[i]
    
    return k

# --------------- Method 2 -----------------
# Using list comprehension
# Time: O(n)
# Space: O(n), where n = len(nums)

def removeElement(nums: list[int], val: int) -> int:
    tmp = [i for i in nums if i != val]
    for i in range(len(tmp)):
        nums[i] = tmp[i]
    return len(tmp)

if __name__ == '__main__':
    # Test Case 1
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement(nums, val))
    print(nums)

     # Test Case 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElement(nums, val))
    print(nums)