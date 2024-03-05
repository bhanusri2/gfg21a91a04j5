#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    
    def maxIndexDiff(self,a, n): 
        # p=[]
        # if n==1:
        #     return 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if a[j]>a[i]:
        #             p.append(j-i)
        # return max(p)
        # md=-1
        # lm=a[0]*n
        # rm=a[0]*n
        # lm[0]=a[0]
        # for i in range(1,n):
        #     lm[i]= min(a[i],lm[i-1])
        # lm[n-1]=a[n-1]
        # for i in range(n - 2, -1, -1):
        #     rm[i]=max(a[i],rm[i+1])
        # i = j = 0
        # while i < n and j < n:
        #     if lm[i] <= rm[j]:
        #         md = max(md, j - i)
        #         j += 1
        #     else:
        #         i += 1
        # return md
        # m=0
        # for i in range(n):
        #     for j in range(n-1,1,-1):
        #         if a[j]>=a[i]:
        #             m=max(m,j-i)
        #             break
        # return m
       
        max_diff = -1
        left_min = [0] * n
        right_max = [0] * n
        left_min[0] = a[0]
        for i in range(1, n):
            left_min[i] = min(a[i], left_min[i - 1])
        right_max[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(a[i], right_max[i + 1])

        i = j = 0
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1
    
        return max_diff


        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends