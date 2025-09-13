class Solution:
    def findElement(self, arr):
        # code here
        
        m1=9999
        m2=-9999
        l1=[]
        for i in range(len(arr)):
            m2=max(m2,arr[i])
            l1.append(m2)
        
        l2=[]
        for i in range(len(arr)-1,-1,-1):
            m1=min(m1,arr[i])
            l2.append(m1)
        l2[::]=l2[::-1]
        for i in range(1,len(arr)-1):
            if l1[i]==l2[i]:
                return arr[i]
        return -1  