//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//Back-end complete function template in C++

class Solution{
	public:
	//Function to find all prime factors of a number.
	vector<int> AllPrimeFactors(int N) {
		vector<int> spf(N+1); //Array to store smallest prime factor for each number.
		vector<int> vis(N+1,false); //Array to mark visited numbers.
		
		//Initializing even numbers with smallest prime factor 2.
		for(int i = 2; i <= N; i+=2)
			spf[i] = 2;

		//Using linear sieve to find smallest prime factor for each odd number.
		for(long long int i = 3; i <= N; i+=2){
			if(!vis[i]){
				spf[i] = i; //Smallest prime factor of prime number is itself.
				
				//Updating smallest prime factor for multiples of current prime number.
				for(long long int j = i; j*i <= (long long int)N; j+=2){
					if(!vis[j*i]){
						spf[j*i] = i; //Updating smallest prime factor.
						vis[j*i] = true; //Marking number as visited.
					}
				}
			}
		}
		
		vector<int> ans; //Vector to store prime factors.
		
		//Finding prime factors by dividing number with its smallest prime factor.
		while(N > 1){
			ans.push_back(spf[N]); //Adding smallest prime factor to the answer vector.
			N /= spf[N]; //Dividing by smallest prime factor to get next prime factor.
		}
		
		sort(ans.begin(), ans.end()); //Sorting prime factors in ascending order.
		ans.resize(unique(ans.begin(), ans.end()) - ans.begin()); //Removing duplicates from prime factors.
		
		return ans; //Returning vector containing all prime factors.
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int N;
		cin >> N;
		Solution ob;
		vector<int>ans = ob.AllPrimeFactors(N);
		for(auto i: ans)
			cout << i <<" ";
		cout <<"\n";
	}  
	return 0;
}
// } Driver Code Ends