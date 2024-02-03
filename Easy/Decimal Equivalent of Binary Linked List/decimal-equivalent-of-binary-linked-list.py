# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
import math
class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        def fun(head):
            current = head
            result = ""
            while current is not None:
                if(current.data):
                    result+="1"
                else:
                    result+='0'
                current = current.next
            return result
        l=fun(head)
        s=0
        p=str(l)
        return (int(l,2)%MOD)
        


#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob=Solution()
        print(ob.decimalValue(list1.head))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends