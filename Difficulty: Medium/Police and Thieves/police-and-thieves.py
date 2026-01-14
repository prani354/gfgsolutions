class Solution:
    def catchThieves(self, arr, k):
        #code here
        police = []
        theif = []
        
        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            else:
                theif.append(i)
                
        i , j = 0 , 0
        count = 0
        
        while i < len(police) and j < len(theif):
            
            if abs(police[i] - theif[j]) <= k:
                count += 1
                i += 1
                j += 1
                
            elif theif[j] < police[i]:
                j += 1
            
            else:
                i += 1
                
        return count
            
                
        

