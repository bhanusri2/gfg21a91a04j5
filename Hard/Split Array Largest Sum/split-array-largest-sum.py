#User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):
        def is_valid(arr, K, max_sum):
            subarray_sum = 0
            subarrays = 1
            for num in arr:
                subarray_sum += num
                if subarray_sum > max_sum:
                    subarray_sum = num
                    subarrays += 1
            return subarrays <= K
        left, right = max(arr), sum(arr)
        while left < right:
            mid = (left + right) // 2
            if is_valid(arr, K, mid):
                right = mid
            else:
                left = mid + 1
        return left 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends