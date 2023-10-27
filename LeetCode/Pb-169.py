# Majority Element

# ---------- Method 1 -------------
# Using a dictionary to store (element, number) pairs
# Time: O(n), but slow
# Space: O(n)

def majorityElement(nums: list[int]) -> int:
    d = {}
    for e in nums:  # make the dictionary
        if e not in d.keys():
            d[e] = 1
        else:
            d[e] += 1

    #   return the key with the largest value
    return max(d, key=lambda k: d.get(k))

# ---------- Method 2 -------------
# Using built-in function list.count()
# Time: O(n**2)
# Space: O(1)
# Time Limit Exceeded 

def majorityElement(nums: list[int]) -> int:
    c = int(len(nums) / 2)
    for i in range(len(nums)):
        if nums.count(nums[i]) > c:
            return nums[i]

# ---------- Method 3 -------------
# Sort the list first then traversal
# Time: O(nlgn)
# Space: O(1)

def majorityElement(nums: list[int]) -> int:
    c = int(len(nums) / 2)
    nums.sort()
    cur = nums[0] # pointer for traversal
    k = 0   # number of appears
    for i in range(len(nums)):
        if nums[i] == cur:
            k += 1
            if k > c:
                return nums[i]
        else:
            cur = nums[i]
            k = 1

# ---------- Method 4 -------------
# Sort the list first then return the middle element
# Time: O(nlgn)
# Space: no extra space

def majorityElement(nums: list[int]) -> int:
    nums.sort()
    return nums[int(len(nums)/2)]
    
if __name__ == '__main__':
    # Test Case 1
    nums = [3, 2, 3]
    print(majorityElement(nums))

    # Test Case 1
    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))
 
   