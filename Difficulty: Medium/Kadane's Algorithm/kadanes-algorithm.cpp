class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        // Code here
        int curr_sum = 0;
        int max_sum = INT_MIN;
        int n = arr.size();
        
        for (int i = 0;i<n;i++){
            curr_sum = curr_sum+arr[i];
            
            max_sum = max(max_sum,curr_sum);
            
            if (curr_sum < 0){
                curr_sum = 0;
            }
        }
        
        return max_sum;
    }
};