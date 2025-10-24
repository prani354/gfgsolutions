from collections import Counter, defaultdict

class Solution:

    def isPossible(self, arr, k):
        # Code here
        count = Counter(arr)  
        need = defaultdict(int)  
    
        for num in arr:
            if count[num] == 0:
                continue
    
            
            if need[num - 1] > 0:
                need[num - 1] -= 1
                need[num] += 1
                count[num] -= 1
            else:
                
                can_start = True
                for i in range(num, num + k):
                    if count[i] == 0:
                        can_start = False
                        break
                if not can_start:
                    return False
                
                for i in range(num, num + k):
                    count[i] -= 1
                need[num + k - 1] += 1  
    
        return True
                
        