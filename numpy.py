#Q1

import numpy as np
a=np.random.random(10).reshape(10,1)
mean=np.mean(a)
print(mean)

#Q2

b=np.random.random(20).reshape(20,1)
sd=np.std(b)
var=np.var(b)
print(sd,var)

#Q3

A=np.random.random(200).reshape(10,20)
B=np.random.random(500).reshape(20,25)
C=np.dot(A,B)
print(np.sum(C))

#Q4
A=np.random.random(10).reshape(10,1)
B=1/(1+np.exp(-A))
print("New Array:\n",B)