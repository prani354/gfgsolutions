#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        s = height[0]
        can_see = 1
        
        for i in range(1,len(height)):
            if height[i] > s:
                s = height[i]
                can_see += 1
                
        return can_see