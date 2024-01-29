//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	int dp[101][901];
	int fun(int ind,int c,int p,int n,string &str){
	    if(ind==n)return 1;
	    if(dp[ind][p]!=-1)
	    {
	        return dp[ind][p];
	    }
	    int x = 0;
	    int ans = 0;
	    for(int i=ind;i<str.size();i++){
	      x += str[i]-'0';
	      if(x >= p)
	      {
	          ans+=fun(i+1,0,x,n,str);
	      }
	      
	    }
	    return dp[ind][p] = ans;
	}
	int TotalCount(string str){
	    memset(dp,-1,sizeof(dp));
	    int n=str.size();
        return fun(0,0,0,n,str);
        
        
    
	}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string str;
		cin >> str;
		Solution ob;
		int ans = ob.TotalCount(str);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends