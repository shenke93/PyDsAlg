# Remove Element

# --------------- Method 1 -----------------
# Using a support list
# Time: O(n)
# Space: O(n), where n = len(nums)

def removeDuplicates(nums: list[int]) -> int:  
    res = []

    # Initialize with len(nums) == 1
    cur = nums[0]
    res.append(cur)
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != cur: # find a non-duplicated element
            cur = nums[i]
            k += 1 
            res.append(cur)

    # copy to nums
    for i in range(len(res)):
        nums[i] = res[i]

    return k

# --------------- Method 2 -----------------
# Using two pointers
# Time: O(n**2)
# Space: no extra space needed

def removeDuplicates(nums: list[int]) -> int:  
    i = 0   # i -> current non-duplicate elements, 
    j = 1   # j -> traversal helper
    if len(nums) == 1:
        return j
    
    while (i < len(nums)) and (j < len(nums)):
        if nums[j] != nums[i]:
            i += 1
            j += 1
        else:
            del nums[j] # O(n)
    return i+1

# --------------- Method 3 -----------------
# Using one pointer
# Time: O(n**2)
# Space: no extra space needed

def removeDuplicates(nums: list[int]) -> int:  
    cur = nums[0]
    k = 1

    i = 1
    while i < len(nums):
        if nums[i] == cur:
            del nums[i] # O(n)
        else: 
            cur = nums[i]
            i += 1
            k += 1
    return k


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
    print(nums)

     # Test Case 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)