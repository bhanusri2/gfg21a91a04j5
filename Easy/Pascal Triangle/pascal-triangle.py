#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    if n==1:
	        return [1]
	    l=[[1],[1,1]]
	    mod=10**9+7
	    for i in range(1,n+1):
	        lst=[1,1]
	        l1=l[i]
	        for j in range(1,i+1):
	            lst.insert(j,(l1[j]+l1[j-1])%mod)
	        l.append(lst)
	    return l[n-1]
	     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends