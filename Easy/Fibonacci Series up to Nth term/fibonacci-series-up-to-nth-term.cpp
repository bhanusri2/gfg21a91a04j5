//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<long long> Series(int N) {
        // COde here
        vector<long long>res;
        if(N==1){
            res.push_back(0);
            res.push_back(1);
            return res;
        }
        else{
            res=Series(N-1);
        }
        res.push_back(res[N-1]+res[N-2]);
        return res;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution obj;

        vector<long long> ans = obj.Series(n);
        for (auto x : ans) cout << x << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends