#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr,n):
		# code here'
		res=arr[0]
		for i in range(n):
		    mul=arr[i]
		    for j in range(i+1,n):
		        res=max(res,mul)
		        mul*=arr[j]
		    res=max(res,mul)
		return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends