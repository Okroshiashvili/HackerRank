"""
Created on Tue May 22 16:53:27 2018

@author: Nodar.Okroshiashvili
"""


import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    

    from collections import deque
    def levelOrder(self,root):      

        queue = self.deque([root]) if root else self.deque()

        while queue:
            node = queue.popleft()
            print(node.data, end=' ')

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
  


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

