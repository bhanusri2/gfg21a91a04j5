#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		arr1=[None]*(n*n)
        arr2=[None]*(n*n)
        idx=0
        for i in range(n):
            for j in range(n):
                arr1[idx]=mat1[i][j]
                arr2[idx]=mat2[i][j]
                idx+=1
        res=0
        left=0
        right=(n*n)-1
        while left<(n*n) and right>=0:
            if arr1[left]+arr2[right]==x:
                res+=1
                left+=1
                right-=1
            elif arr1[left]+arr2[right]<x:
                left+=1
            elif arr1[left]+arr2[right]>x:
                right-=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends