//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    bool detect(int i,int par,vector<int>adj[],int vis[]){
        vis[i]=1;
        for(auto it:adj[i]){
            if(!vis[it]){
                if(detect(it,i,adj,vis)==true)
                return true;
            }else if(par!=it)return true;
        }
        return false;
    }
    public:
	int detectCycle(int V, vector<int>adj[])
	{
	    int vis[V]={0};
        for(int i=0;i<V;i++){
            if(!vis[i]){
                if(detect(i,-1,adj,vis)==true)
                return true;
            }
        }
        return false;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
		cin >> V >> E;
		vector<int>adj[V];
		for(int i = 0; i < E; i++){
			int u, v;
			cin >> u >> v;
			adj[u].push_back(v);
			adj[v].push_back(u);
		}
		Solution obj;
		int ans = obj.detectCycle(V, adj);
		cout << ans <<"\n";	}
	return 0;
}
// } Driver Code Ends