#User function Template for python3
import collections
class Solution:
   
	def hasArrayTwoCandidates(self,arr, n, x):
	    c=0
	    i=0
	    j=len(arr)-1
	    d=collections.Counter(arr)
	    for i in arr:
	        if x-i in d:
	            if x-i!=i:return True
	            elif d[x-i]>1:
	                return True
        return False	                
	                
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends