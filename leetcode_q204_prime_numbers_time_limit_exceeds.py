#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:27:32 2018

@author: aditikulkarni
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        vis = []
        if n%2==0:
            end = n-1
        else:
            end =1
        if (n<=2):
            return 0
        elif (n==3):
            return 1
        elif (n==4):
            return 2
        else:
            lst = []
            for i in range(1,n):
                lst.append(0)
                vis.append(False)
            lst[1] = 1
            for i in range(1,n,2):
                if(i%2==0):
                    vis[i-1] = True
            
            for i in range(3,n,2):
                cnt = 0
                end = i
                if vis[i-1] == False:
                    for j in range(2,end):
                        cnt = j
                        if(i!=j and i%j==0):   
                            break
                        
                    print(i)
                    print("count",cnt)
                    print(end)
                    print(int(i/2)-1)
                    if cnt == (end-1):
                        lst[i-1]=1
                    
                    k=1
                    while k*i<n:
                        vis[k*i-1]=True
                        k+=1
                    
        c = sum(lst)
        print(lst)
        return c

    def countPrimes_efficient(self, n):
        """
        :type n: int
        :rtype: int
        """
        vis = []
        if (n<=2):
            return 0
        elif (n==3):
            return 1
        elif (n==4):
            return 2
        else:
            lst = []
            for i in range(n):
                lst.append(0)
                vis.append(False)
            for num in range(1,n,2):
                if(num%2==0):
                    vis[num-1] = True
            lst[1] = 1
            lst[2]=1
            
            for num in range(5,n,2):
                if(vis[num-1])==False:
                    if((num+1)%6==0 or (num-1)%6==0):
                        lst[num-1]=1
                        k=1
                        while k*num<n:
                            vis[k*num-1]=True
                            k+=1
        c = sum(lst)
        #print(lst)
        return c
                        
                
            
        
                
            
soln = Solution()
print(soln.countPrimes(10)) 
print(soln.countPrimes_efficient(10)) 