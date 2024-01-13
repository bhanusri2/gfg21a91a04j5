#User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        def fun(head):
            current=head
            l=[]
            while current is not None:
                l.append(current.data)
                current=current.next
            return l
        p=fun(head)
        for i in p:
            if i==key:
                return 1
        else:
            return 0
      

#{ 
 # Driver Code Starts


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = list(map(int, input().strip().split()))
        head = Node(data[0])
        tail = head
        for i in range(1, n):
            tail.next = Node(data[i])
            tail = tail.next
        key = int(input())
        ob = Solution()
        res = ob.searchKey(n, head, key)
        print(res)
# } Driver Code Ends