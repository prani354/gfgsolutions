class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        n = len(arr)
        
        # Step 1: Transform array to +1 / -1
        nums = []
        for num in arr:
            if num > k:
                nums.append(1)
            else:
                nums.append(-1)
        
        # Step 2: Compute prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Step 3: Build decreasing stack of indices
        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)
        
        # Step 4: Traverse from right to left
        max_len = 0
        for j in range(n, -1, -1):
            while stack and prefix[j] > prefix[stack[-1]]:
                max_len = max(max_len, j - stack[-1])
                stack.pop()
        
        return max_len
        