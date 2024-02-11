#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        p=[0]*n
        l=set([0])
        for i in range(1,n):
            if p[i-1]-i>0 and (p[i-1]-i) not in l:
                p[i]=p[i-1]-i
                l.add(p[i])
            else:
                p[i]=p[i-1]+i
                l.add(p[i])
        return p
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends