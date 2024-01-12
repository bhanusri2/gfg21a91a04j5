#User function Template for python3

class Solution:
    def countPrimes(self,L,R):
        # def primes(n):
        #     primes=[True]*(n + 1)
        #     primes[0]=primes[1]=False
        #     p=2
        #     while p*p<=n:
        #         if primes[p]==True:
        #             for i in range(p*p,n+1,p):
        #                 primes[i] = False
        #         p+=1
        #     return primes
        # c=0
        # l=primes(R)
        # for i in range(L,R):
        #     if l[i]==True:
        #          c+=1
        # return c
        p = [True] * (R + 1)
        p[0] = False
        p[1] = False
        for i in range(2, (int(R ** 0.5)) + 1):
            if p[i]:
                for j in range(i + i, R + 1, i):
                    p[j] = False
        a = [i for i in range(L, R + 1) if p[i]]
        return len(a)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        L,R=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.countPrimes(L,R)
        print(ans) 
# } Driver Code Ends