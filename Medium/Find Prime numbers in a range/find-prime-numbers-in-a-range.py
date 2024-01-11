#User function Template for python3

class Solution: 
    
    def primeRange(self,M,N):
        def sieve(N):
            primes=[True]*(N+1)
            primes[0]=primes[1]=False
            for i in range(2,int(N**0.5)+1):
                if primes[i]==True:
                    for j in range(i*i,N+1,i):
                        primes[j]=False
            return primes
        k=sieve(N)
        p=[]
        for i in range(M,N+1):
            if k[i]==True:
                p.append(i)
        return p

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends