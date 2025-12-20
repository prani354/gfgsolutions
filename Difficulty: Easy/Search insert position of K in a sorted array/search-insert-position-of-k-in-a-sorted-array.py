import bisect
class Solution:
    def searchInsertK(self, arr, k):
        # code here
        return bisect.bisect_left(arr,k)