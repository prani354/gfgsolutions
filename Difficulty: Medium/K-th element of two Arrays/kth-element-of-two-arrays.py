class Solution:
    def kthElement(self, a, b, k):
        # code here
        a.extend(b)
        a.sort()
        return a[k-1]
        
                
                
        