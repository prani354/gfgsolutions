class Solution:
    def sort012(self, arr):
        # code here
        zero = 0
        one = 0
        two = 0
        
        for i in range(len(arr)):
            if arr[i] == 0:
                zero += 1
            
            elif arr[i] == 1:
                one += 1
                
            else:
                two += 1
                
        
        for j in range(len(arr)):
            
            
            if zero != 0:
                arr[j] = 0
                zero -= 1
                
            elif one != 0:
                arr[j] = 1
                one -= 1
                
            else:
                arr[j] = 2
                two -= 1
                
                