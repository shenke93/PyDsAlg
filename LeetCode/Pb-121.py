# Best Time to Buy and Sell Stock

# ---------- Method 1 -------------
# Using 2 loops
# Time: O(n**2), time limited exceeded
# Space: O(1)

def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(len(prices)-1): # Buy day
        for j in range(i, len(prices)): # Sell day
            diff = prices[j] - prices[i]
            if diff > profit:
                profit = diff
    return profit

# ---------- Method 2 -------------
# Change to the maximun subarray problem
# Time: O(n)
# Space: O(n)

def maxProfit(prices: list[int]) -> int:
    diff = []
    for i in range(len(prices)-1):
        diff.append(prices[i+1] - prices[i])
    return maxSubSum(diff)
   
def maxSubSum(nums: list[int]) -> int:
    max_ending_here = max_so_far = 0
    for e in nums:
        max_ending_here = max(max_ending_here + e, e) # extend the subarray with e, or start with e
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
    

if __name__ == '__main__':

    # Test Case 1
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))

    # Test Case 2
    prices = [7, 6, 4, 3, 1]
    print(maxProfit(prices))