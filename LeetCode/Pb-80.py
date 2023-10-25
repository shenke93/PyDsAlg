# Remove Duplicates from Sorted Array II

# --------------- Method 1 -----------------
# Using one pointer
# Time: O(n**2)
# Space: no extra space needed

def removeDuplicates(nums: list[int]) -> int:  
    cur = nums[0]
    cur_appears = 1
    k = 1

    i = 1
    while i < len(nums):
        if nums[i] == cur:
            cur_appears += 1
            if cur_appears > 2: # Remove element
                del nums[i] # O(n)
            else:  # Keep element
                i += 1
                k += 1
        else: 
            cur = nums[i]
            cur_appears = 1
            i += 1
            k += 1
    return k




if __name__ == '__main__':
    # Test Case 1
    nums = [1,1,1,2,2,3]
    print(removeDuplicates(nums))
    print(nums)

     # Test Case 2
    nums = [0,0,1,1,1,1,2,3,3]
    print(removeDuplicates(nums))
    print(nums)