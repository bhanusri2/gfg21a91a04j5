#User function Template for python3

class Solution:
    def search(self, pat, txt):
        if pat not in txt:
            return [-1]
        n=len(pat)
        i=0
        j=n
        l=[]
        while i<j and j<=len(txt):
            if txt[i:j]==pat:
                l.append(i+1)
            i+=1
            j+=1
        return l
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends