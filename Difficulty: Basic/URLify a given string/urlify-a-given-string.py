class Solution:
    def URLify(self, s): 
        # code here
        string = s.split(" ")
        # print(string)
        
        return "%20".join(string)
        
