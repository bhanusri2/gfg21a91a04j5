# Your task is to complete this function
# Finction should return Integer
class Solution:
    def solve(self, i, j, S, T, dp):
        MOD = 10**9 + 7
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j] % MOD
        if S[i - 1] == T[j - 1]:
            dp[i][j] = (self.solve(i - 1, j - 1, S, T, dp) + self.solve(i - 1, j, S, T, dp)) % MOD
        else:
            dp[i][j] = self.solve(i - 1, j, S, T, dp) % MOD
        return dp[i][j]

    def sequenceCount(self, S, T):
        n = len(S)
        m = len(T)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        return self.solve(n, m, S, T, dp)


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends