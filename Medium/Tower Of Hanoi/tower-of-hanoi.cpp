//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution{
    public:
    // You need to complete this function
    void movedisk(int N,int scr,int help,int des,long long &cnt,int disk){
        if(N>0){
            movedisk(N-1,scr,des,help,cnt,disk);
            cout<<"move disk "<<N<<" from rod "<<scr<< " to rod "<<des<<endl;     
            cnt++;
            movedisk(N-1,help,scr,des,cnt,disk);
        }
    }
    // avoid space at the starting of the string in "move disk....."
    long long toh(int N, int from, int to, int aux) {
           int src=from;
           int des=to;
           int help=aux;
           long long cnt=0;
           int disk=1;
           movedisk(N,src,help,des,cnt,disk);
           return cnt;
       }

};

//{ Driver Code Starts.

int main() {

    int T;
    cin >> T;//testcases
    while (T--) {
        
        int N;
        cin >> N;//taking input N
        
        //calling toh() function
        Solution ob;
        
        cout << ob.toh(N, 1, 3, 2) << endl;
    }
    return 0;
}



// } Driver Code Ends