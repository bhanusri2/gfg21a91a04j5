//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    // Function to return a list containing the DFS traversal of the graph.
    void dfs(int i,vector<int>&vis,vector<int>&ls,vector<int> adj[]){
        vis[i]=1;
        ls.push_back(i);
    
        for(auto it:adj[i]){
            if(!vis[it]){
                dfs(it,vis,ls,adj);
            }
        }
    }
    vector<int> dfsOfGraph(int V, vector<int> adj[]) {
       vector<int>vis(V+1,0);
       vector<int>ls;
       int i=0;
       dfs(i,vis,ls,adj);
       return ls;
       
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >> E;

        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        // string s1;
        // cin>>s1;
        Solution obj;
        vector<int> ans = obj.dfsOfGraph(V, adj);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends