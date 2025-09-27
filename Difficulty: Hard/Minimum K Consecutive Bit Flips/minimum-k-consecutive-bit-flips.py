class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n = len(arr)
        flips = 0
        count = 0
        
        for i in range(n):
            if i >= k and arr[i-k] == 2:
                count ^= 1
                
            if arr[i] ^ count == 0:
                if i + k > n:
                    return -1
                flips += 1
                count ^= 1
                arr[i] = 2
                
        return flips
                