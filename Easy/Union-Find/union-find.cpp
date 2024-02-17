//{ Driver Code Starts
//Initial Template for C++


#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution
{
    
    public:
    int Findparent(int node,int par[]){
        if(par[node]==node)return node;
        return Findparent(par[node],par);
    }
    //Function to merge two nodes a and b.
    void union_( int a, int b, int par[], int rank1[]) 
    {
        a=Findparent(a,par);
        b=Findparent(b,par);
        if(rank1[a]>rank1[b]){
            par[b]=a;
            rank1[a]++;
        }
        else{
            par[a]=b;
            rank1[b]++;
        }
        
    }
    
    //Function to check whether 2 nodes are connected or not.
    bool isConnected(int x,int y, int par[], int rank1[])
    {
        int p1=Findparent(x,par);
        int p2=Findparent(y,par);
        if(p1==p2){
           return true;
         }
         else{
             return false;
         }
    }

};

//{ Driver Code Starts.

int main() {
    //taking number of testcases
    int t;
    cin>>t;
    while(t--) {
        
        //taking number of elements
        int n;
        cin>>n;
        
        
        int par[n+1];
        int rank1[n+1];

        //initializing the parent and
        //the rank array
        for(int i=1; i<=n; i++) {
            par[i] = i;
            rank1[i] = 1;
    }
    
    //taking number of queries
    Solution obj;
    int q;
    cin>>q;
    while(q--) {    
        int a,b;
        char c;
        cin>>c>>a>>b;
        
        //if query type is 'U'
        //then calling union_ method
        if(c=='U')
        {
            obj.union_(a,b, par, rank1);
        }
        else//else calling isConnected() method
        cout<<obj.isConnected(a,b, par, rank1)<<endl;
    }
    }
    return 0;
}

// } Driver Code Ends