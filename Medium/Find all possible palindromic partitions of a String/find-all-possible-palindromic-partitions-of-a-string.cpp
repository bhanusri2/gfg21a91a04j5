//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
  void fun(int ind,int n,string &S,vector<string>&temp,vector<vector<string>>&ans){
      if(ind==n){
          ans.push_back(temp);
          return;
      }
      for(int i=ind;i<n;i++){
          string str=S.substr(ind,i-ind+1);
          if(str==string(str.rbegin(),str.rend())){
              temp.push_back(str);
              fun(i+1,n,S,temp,ans);
              temp.pop_back();
          }
          
      }
  }
    vector<vector<string>> allPalindromicPerms(string S) {
        // code here
        int n=S.size();
        vector<string>temp;
        vector<vector<string>>ans;
        fun(0,n,S,temp,ans);
        return ans;        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        
        cin>>S;

        Solution ob;
        vector<vector<string>> ptr = ob.allPalindromicPerms(S);
        
        for(int i=0; i<ptr.size(); i++)
        {
            for(int j=0; j<ptr[i].size(); j++)
            {
                cout<<ptr[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    return 0;
}
// } Driver Code Ends