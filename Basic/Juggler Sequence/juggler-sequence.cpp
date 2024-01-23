//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
void solve(int n,vector<int>&v){
    if (n==1){
        v.push_back(1);
        return;
    }
    if(n&1){
        v.push_back(n);
        int num=pow(n,1.5);
        solve(num,v);
    }
    else{
        v.push_back(n);
        int num=pow(n,0.5);
        solve(num,v);
    }
}
    vector<int> jugglerSequence(int N){
        // code here
        vector<int>ans;
        solve(N,ans);
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        vector<int> ans = ob.jugglerSequence(N);
        for(int u: ans)
            cout<<u<<" ";
        cout<<endl;
    }
    return 0;
}
// } Driver Code Ends