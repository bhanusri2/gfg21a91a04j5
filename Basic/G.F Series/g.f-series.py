class Solution:
    def gfSeries(self, N : int) -> None:
        fib1 = 0
        fib2 = 1
        fib = 0
        if(N == 1):
            print(fib1)
        if(N == 2):
            print(fib1,fib2)
        else:
            print(fib1,fib2,end = " ")
            for i in range(2,N):
                fib = fib1**2 - fib2
                print(fib,end = " ")
                fib1 = fib2
                fib2 = fib
        print()



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        obj.gfSeries(N)

# } Driver Code Ends