#User function Template for python3
class Solution:
    def removeDuplicates(self, s):
        # str_list = list(s)
        # i = 0
        # while i < len(str_list):
        #     j = i + 1
        #     while j < len(str_list):
        #         if str_list[i] == str_list[j]:
        #             str_list.pop(j)
        #         else:
        #             j += 1
        #     i += 1
        # return ''.join(str_list)
        seen = set()
        result = []
        for char in s:
            if char not in seen:
                result.append(char)
                seen.add(char)
        return ''.join(result)


        





#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends