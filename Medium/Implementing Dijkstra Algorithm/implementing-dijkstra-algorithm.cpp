//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

	
	class Solution
{
	public:
    vector <int> dijkstra(int v, vector<vector<int>> adj[], int s)
    {
       vector<int>dis(v,INT_MAX);
       dis[s]=0;
       priority_queue<pair<int,int>>pq;
       pq.push({0,s});
       while(!pq.empty()){
           int node=pq.top().second;
           int wt=-1*pq.top().first;
           
           pq.pop();
           for(auto it:adj[node]){
               if(dis[it[0]]>(wt+it[1])){
                   dis[it[0]] = wt+it[1];
                   pq.push({-1*dis[it[0]],it[0]});
               }
             
           }
           
           
       }
       return dis;
     
    }
};


//{ Driver Code Starts.


int main()
{
    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> adj[V];
        int i=0;
        while (i++<E) {
            int u, v, w;
            cin >> u >> v >> w;
            vector<int> t1,t2;
            t1.push_back(v);
            t1.push_back(w);
            adj[u].push_back(t1);
            t2.push_back(u);
            t2.push_back(w);
            adj[v].push_back(t2);
        }
        int S;
        cin>>S;
        
        Solution obj;
    	vector<int> res = obj.dijkstra(V, adj, S);
    	
    	for(int i=0; i<V; i++)
    	    cout<<res[i]<<" ";
    	cout<<endl;
    }

    return 0;
}


// } Driver Code Ends