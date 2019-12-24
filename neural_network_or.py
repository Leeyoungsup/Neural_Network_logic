import numpy as np
def func(x,T):
    y=np.where(NET>=T,1,0)
    return y
x=np.array([[0,0],[0,1],[1,0],[1,1]])
w=np.array([[1,1]])
NET=np.dot(x,w.T)
T=1
y=func(NET,T)
print(y)