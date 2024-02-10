//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
public:
int c;
int dp[100][100][100];
int fun(int i,int j,int n,int k,vector<vector<int>>&arr,int s){
    if(i<0 or j<0 or i>=n or j>=n or s>k ){
        return 0;
    }
    if(dp[i][j][s]!=-1)return dp[i][j][s];
    if(i==n-1 and j==n-1 and s+arr[i][j]==k)return 1;
    dp[i][j][s]=fun(i+1,j,n,k,arr,s+arr[i][j])+fun(i,j+1,n,k,arr,s+arr[i][j]);
    return dp[i][j][s];
}
    
    long long numberOfPath(int n, int k, vector<vector<int>> &arr){
        c=0;
        memset(dp,-1,sizeof(dp));
        return fun(0,0,n,k,arr,0);
        
    }
};

//{ Driver Code Starts.

int main()
{
    Solution obj;
    int i,j,k,l,m,n,t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        vector<vector<int>> v(n, vector<int>(n, 0));
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                cin>>v[i][j];
        cout << obj.numberOfPath(n, k, v) << endl;
    }
}
// } Driver Code Ends