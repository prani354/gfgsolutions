class Solution {
  public:
    int minJumps(vector<int>& arr) {
        // code here
         int jump = 0;
	    int pos = 0;
	    int des = 0;
	    
	    int n = arr.size();
	    
	    for(int i = 0;i < n-1;i++){
	        des = max(des,i+arr[i]);
	        
	        if (i >= des){
	            return -1;
	        }
	        
	        if (pos == i){
	            pos = des;
	            jump += 1;
	        }
	    }
	    return jump;
    }
};
