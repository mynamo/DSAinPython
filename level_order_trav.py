#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:42:38 2018

@author: aditikulkarni
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            depth = 0
            lst = []
            level =[]
            level =[0]
            head = root
            #rtnode = head
            ilst = []
            rt = []
            #print(root.val)
            rt.append(root)
            #print(rt)
            #parent = head
            level = [0]
            l = [root]
            while rt:
                #print("level " + str(level[0]))
                #print(l)
                depth +=1
                root = rt[0]
                rt.remove(root)
                if root.left is not None:
                    l.append(root.left)
                    rt.append(root.left)
                    #marked.append(True)
                    level.append(level[0]+1)
                if root.right is not None:
                    l.append(root.right)
                    rt.append(root.right)
                    #marked.append(True)
                    level.append(level[0]+1)
                
                
                levp = level[0]
                level.remove(level[0])
                #marked.remove(marked[0])
                if (len(level)>0 and levp!=level[0]):
                    lst.append(l)
                    l = [rt[0]]
                #print(rt)
            #print(lst)
            #lst.remove(lst[-1])
            for i,l in enumerate(lst):
                l_t= []
                l_ = lst[len(lst)-i-1][1:]
                if len(l_)>0:
                    for x in l_:
                        l_t.append(x.val)
                if len(l_t)>0:
                    ilst.append(l_t)
            ilst.append([head.val])
            #if(len(ilst)>1):
            #    ilst.remove(ilst[0])
            #print(lst)
            #print(ilst)
        else:
            ilst = []
        return ilst
    
rn = TreeNode(3)
ln1 = TreeNode(9)
rn1 =  TreeNode(20)
ln11 = TreeNode(19)
rn12 = TreeNode(7)
rn.left = ln1
rn.right = rn1
rn1.left = ln11
rn1.right = rn12
soln = Solution()
res = soln.levelOrderBottom(rn)
print(res)