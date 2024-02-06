#User function Template for python3
from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        # d1 = {}
        # if len(words) == 2:
        #     for i in words:
        #         if i not in d1:
        #             d1[i] = 1
        #         else:
        #             d1[i] += 1
        #     return [d1.keys()]
            
        # def fun(n):
        #     l=["0"]*26
        #     for i in n:
        #         l[ord(i)-97]="1"
        #     return int("".join(l),2)
        # lst=[]
        # d={}
        # for i in words:
        #     lst.append(fun(i))
        # for i in range(len(lst)):
        #     if lst[i] not in d:
        #         d[lst[i]]=[words[i]]
        #     else:
        #         ll=d[lst[i]]
        #         ll.append(words[i])
        #         d[lst[i]]=ll
        # return [*d.values()]
        l=defaultdict(list)
        for i in words:
            l["".join(sorted(i))].append(i)
        return l.values()
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends