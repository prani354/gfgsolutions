class Solution {
  public:
    int getSecondLargest(vector<int> &arr) {
        // code here
        set<int> s (arr.begin(),arr.end());
        vector<int> v(s.begin(),s.end());
        sort(v.begin(),v.end());
        int n = v.size();
        
        if (v.size()< 2){
            return -1;
        }
        return v[n-2];
        
    }
};