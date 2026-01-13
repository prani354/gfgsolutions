class Solution:
    def canServe(self, arr):
        # code here 
        n = len(arr)
        five = 0
        ten = 0
        twenty = 0
        
        for i in range(n):
            if arr[i] == 5:
                five += 1
                
            elif arr[i] == 10:
                ten += 1
                
                if five >= 1:
                    five -= 1
                else:
                    return False
                
                
            else:
                twenty += 1
                
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                    
                elif five >= 3:
                    five -= 3
                    
                else:
                    return False
                
            
        return True
                
            
            
            
            
            
        