class Solution {
  public:
    void sort012(vector<int>& arr) {
        // code here
        int n = arr.size();
        // vector<int> v(n,0);
        int one=0;
        int two = 0;
        int zero = 0;
        
        
        for (int x : arr){
            if (x == 0){
                zero += 1;
            }
        
            if (x == 1){
                one += 1;
            }
            
            if (x == 2){
                two += 1;
            }
        }
        
        for (int j = 0;j<n;j++){
            if (zero != 0){
                arr[j] = 0;
                zero -= 1;
            }
            else if (one != 0){
                arr[j] = 1;
                one -= 1;
            }
            else if (two != 0){
                arr[j] = 2;
                two -= 1;
            }
        }
    
    }
};