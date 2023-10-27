# Rotate Array

# ---------- Method 1 -------------
# Using list methods
# Time: O(n**2)
# Space: O(1)

def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_font_index = (0 + k) % len(nums)
        for _ in range(new_font_index):
              nums.insert(0, nums.pop())

# ---------- Method 2 -------------
# Using list methods, but not insert()
# Time: O(n**2)
# Space: O(1)

def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_font_index = (0 + k) % len(nums) # same as n_shift
        k = len(nums) - new_font_index # non_shift numbers

        for i in range(k):  # copy non_shift numbers at the end 
               nums.append(nums[i]) 

        for i in range(k):  # delete non_shift numbers at the front 
               del nums[0]

# ---------- Method 3 -------------
# Using extend and list index, same logic as method 2
# Time: O(n)
# Space: O(n)

def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_font_index = (0 + k) % len(nums) # same as n_shift
        k = len(nums) - new_font_index # remain number of elements

        nums.extend(nums[:k])
        nums[:] = nums[k:]
    
        
    
if __name__ == '__main__':
    # Test Case 1
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums, k)
    print(nums)

    # Test Case 2
    nums = [-1,-100,3,99]
    k = 2
    rotate(nums, k)
    print(nums)
 
   