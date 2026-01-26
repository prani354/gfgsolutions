class Solution:
    def permuteDist(self, arr):
        # code here
        def permutations(res, arr, idx):
            if idx == len(arr):
                res.append(arr[:])
                return
        
            # Permutations made by swapping each element starting from index `idx`
            for i in range(idx, len(arr)):
                # Swapping
                arr[idx], arr[i] = arr[i], arr[idx]
        
                # Recursive call
                permutations(res, arr, idx + 1)
        
                # Backtracking
                arr[idx], arr[i] = arr[i], arr[idx]
        res = []
        permutations(res, arr, 0)
        return res
            
        
        
        