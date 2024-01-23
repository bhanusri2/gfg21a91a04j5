//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++
class Solution
{
public:
    void gfSeries(int N)
    {
        // Write Your Code here
        long long a = 0;
        long long b = 1;
        N -= 2;
        cout << a << " " << b << " ";
        while(N--){
            long long c = (a*a)-b;
            a = b;
            b = c;
            cout<<c<<" ";
        }
        cout << endl;
        return;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        Solution ob;
        ob.gfSeries(N);
    }
    return 0;
}
// } Driver Code Ends