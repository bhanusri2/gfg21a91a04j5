#User function Template for python3

class Solution:
    def primeProduct(self, a,b):
        p=1
        def prime(n):
            l=[1 for i in range(n+1)]
            l[0],l[1]=0,0
            m=[]
            for i in range(2,int(n**0.5)+1):
                if(l[i]==1):
                    for j in range(i*i,n+1,i):
                        l[j]=0
            for i in range(2,len(l)):
                if(l[i]==1):
                    m.append(i)
            return m
        s=prime(int(b**0.5))
        m=[i for i in range(a,b+1)]
        for i in s:
            if(a%i==0):
                for j in range(0,len(m),i):
                    if(m[j]!=i):
                        m[j]=0
            else:
                c=((a//i)*i)+i
                k=(c-a)
                for j in range(k,len(m),i):
                    if(m[j]!=i):
                        m[j]=0
        for i in m:
            if(i!=0):
                p=(p*i)%(1000000007)
        return p%1000000007
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.primeProduct(L, R))
# } Driver Code Ends