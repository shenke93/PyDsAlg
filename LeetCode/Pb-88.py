# Merge Sorted Array

# ---------- Method 1 -------------
# Copy all elements in list1 and then sort list 1
# Time: O(nlgn)
# Space: O(n), where n is len(nums1)

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()   

# ---------- Method 2 -------------
# Using 2 pointers
# Time: O(n)
# Space: O(n)

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0 # i pointer over nums1; j pointer over nums 2;
        t = []
        while (i < m) and (j < n):      
            if nums1[i] <= nums2[j]:
                 t.append(nums1[i])
                 i += 1
            else:
                 t.append(nums2[j])
                 j += 1

        if (i == m):    # if nums 1 is finished
            while j < n:
                 t.append(nums2[j])
                 j += 1
        
        if (j == n):    # if nums 2 is finished
            while i < m:
                 t.append(nums1[i])
                 i += 1

        for i in range(len(t)):
             nums1[i] = t[i]
    
if __name__ == '__main__':
    
    # Test Case 6
    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    merge(nums1, 1, nums2, 5)
    print(nums1)

    # Test Case 4
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 3, nums2, 3)
    print(nums1)

    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    print(nums1)

    # Test Case 2
    nums1 = [1]
    nums2 = []
    merge(nums1, 1, nums2, 0)
    print(nums1)

    # Test Case 3
    nums1 = [0]
    nums2 = [1]
    merge(nums1, 0, nums2, 1)
    print(nums1)

   