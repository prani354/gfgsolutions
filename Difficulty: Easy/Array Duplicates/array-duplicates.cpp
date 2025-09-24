class Solution {
  public:
    vector<int> findDuplicates(vector<int>& arr) {
        // code here
        vector<int> v;
        map<int,int> m;
        
        for (int x:arr){
            m[x] += 1;
        }
        
        for (auto y:m){
            if (y.second > 1){
                v.push_back(y.first);
            }
        }
        
        return v;
    }
};