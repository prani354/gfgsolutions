class Solution:
    def inversionCount(self, arr):
        # Code Here
        def merge_sort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            
            inv = 0
            inv += merge_sort(left, mid)  # merge sort by dividing the array into two divisions 
            inv += merge_sort(mid + 1, right) #Same as previous dtep but for the next half
            inv += merge(left, mid, right)  #Now  merging it by using divide and conquer method
            
            return inv
        
        def merge(left, mid, right):
            temp = []
            i = left
            j = mid + 1
            inv_count = 0
            
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])  
                    inv_count += (mid - i + 1) #This is the difference for which inversion count is counted 
                    j += 1
            
            while i <= mid:
                temp.append(arr[i])
                i += 1
            
            while j <= right:
                temp.append(arr[j])
                j += 1
            
            # Copy back
            for k in range(len(temp)):
                arr[left + k] = temp[k]
            
            return inv_count
        
        return merge_sort(0, len(arr) - 1)
        
        