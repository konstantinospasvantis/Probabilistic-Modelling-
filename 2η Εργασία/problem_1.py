# -*- coding: utf-8 -*-
"""Problem_1_Probabilities.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yIwHPGoA25BESkNxI7DbXDcYKvm-gcYg
"""

import numpy as np
import math

def Prob_1_KLD(file):
  f=open(file,'r')
  s=f.readlines()
  A=np.fromstring(s[0][:-1],dtype=float,sep=' ')
  for i in range(1,len(s)):
   A1=np.fromstring(s[i][:-1],dtype=float,sep=' ')
   A=np.vstack([A,A1])
  min=1 #we use this variable to compare it to the KLD 
  KLD=0 #KUllback-Leibler Divergence
  t=0  #variable that iterates through distributions that are different from our first
  ROW=np.zeros(A.shape[0])
  for i in range(A.shape[0]):
    for t in range(A.shape[0]):
      for j in range(A.shape[1]):
        if t==i :
          pass
        elif t!=i:
          KLD=KLD+A[i,j]*(log(A[i,j]/A[t,j],10))
      if KLD<min and KLD!=0:
        min=KLD
        ROW[i]=t+1
      KLD=0    
    min=1
  return(ROW)

def Prob_1_MI(file):
  f=open(file,'r')
  s=f.readlines()
  A=np.fromstring(s[0][:-1],dtype=float,sep=' ')
  for i in range(1,len(s)):
     A1=np.fromstring(s[i][:-1],dtype=float,sep=' ')
     A=np.vstack([A,A1])
  Total=0
  for i in range(A.shape[0]):
    Total=Total+sum(A[i])
  A=np.divide(A,Total)
  MI=0
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      MI=MI+A[i,j]*log(A[i,j]/(sum(A[i])*sum(A[:,j])),10)
  return MI