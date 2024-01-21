#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
         
        st=[]
        ans=[0]*n
        ans[-1]=-1
        st.append(arr[-1])
        for i in range(n-1,-1,-1):
            while (st!=[] and st[-1]<=arr[i]):
                st.pop()
            if (st!=[] and st[-1]>arr[i]):
                ans[i]=st[-1]
                st.append(arr[i])
            if (st==[]):
                ans[i]=-1
                st.append(arr[i])
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends