//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
    void dfs(int i,vector<vector<int>>&adj,vector<bool>&visited,stack<int>&s)
    {
    visited[i]=1;
    for(auto it:adj[i]){
        if(!visited[it]){
           dfs(it,adj,visited,s);
        }

    }
    s.push(i);
}
    
	public:
	//Function to find number of strongly connected components in the graph.
    int kosaraju(int V, vector<vector<int>>& adj)
    {
      stack<int>s;
      vector<bool>visited(V,false);
      for(int i=0;i<V;i++){
          if(!visited[i]){
              dfs(i,adj,visited,s);
              }
          }
         
        vector<vector<int>>rev(V+1);
        vector<bool>visited1(V,false);
        for(int i=0;i<V;i++){
            for(auto it:adj[i]){
                rev[it].push_back(i);
            }
        }
       int count=0;
        while(!s.empty()){
            stack<int>sad;
            int temp=s.top();
            // cout<<temp;
            s.pop();
            if(!visited1[temp]){
                count++;
                dfs(temp,rev,visited1,sad);
            }
            
        }
        return count;
    }
      
    
};

//{ Driver Code Starts.


int main()
{
    
    int t;
    cin >> t;
    while(t--)
    {
    	int V, E;
    	cin >> V >> E;

    	vector<vector<int>> adj(V);

    	for(int i = 0; i < E; i++)
    	{
    		int u, v;
    		cin >> u >> v;
    		adj[u].push_back(v);
    	}

    	Solution obj;
    	cout << obj.kosaraju(V, adj) << "\n";
    }

    return 0;
}


// } Driver Code Ends