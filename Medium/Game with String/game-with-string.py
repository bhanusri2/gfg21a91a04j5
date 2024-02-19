#User function Template for python3

class Solution:
    def minValue(self, s, k):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=list(d.values())
        for i in range(k):
            l.sort()
            p=l[-1]
            p=p-1
            l[-1]=p
        s=0
        for i in l:
            s+=i*i
        return s
              
             
             
            
            
            
            
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends