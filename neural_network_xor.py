import numpy as np
def func(x,T):
    y=np.where(NET>=T,1,0)
    return y
x=np.array([[0,0],[0,1],[1,0],[1,1]])
w=np.array([[1,1]])
NET=np.dot(x,w.T)
T=1
z1=func(NET,T)
T=2
z2=func(NET,T)
z2=np.where(z2==1,0,1)
z=np.hstack((z1,z2))
NET=np.dot(z,w.T)
T=2
y=func(NET,T)

print(y)