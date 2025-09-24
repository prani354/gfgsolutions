class Solution {
  public:
    int majorityElement(vector<int>& arr) {
        // code here
        int n = arr.size();
        map<int,int> m;
        
        for(auto x: arr){
            m[x] += 1;
        }
        
        int max_val = n / 2;
        int res = INT_MAX;
        
        for (auto y:m){
            if(y.second > max_val){
                res = y.first;
            }
        }
        
        if (res == INT_MAX){
            return -1;
        }
        
        return res;
    }
};