#User function Template for python3
class Solution:
    def leastPrimeFactor (self, n):
        # def least_prime(n):
        least_prime = [0] * (n + 1)
        least_prime[1] = 1
        for i in range(2, n + 1) :
            if (least_prime[i] == 0) :
                least_prime[i] = i
                
                for j in range(i * i, n + 1, i) :
                    if (least_prime[j] == 0) :
                        least_prime[j] = i
        return least_prime

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.leastPrimeFactor(n)
		for i in range(1, n+1):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends