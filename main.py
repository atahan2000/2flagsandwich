import matplotlib.pyplot as plt
import numpy as np



def FIRSTflagsandwich(values, flag1 = 0, flag2 = 1):
    while np.any(abs(flag2-flag1)>0.0001):
        flag1 += np.divide(np.abs(flag1-flag2),values)
        flag2 -= np.divide(np.abs(flag1-flag2),values)
    return flag1

def SECONDflagsandwich(values, flag1 = 0, flag2 = 1):
    while np.any(abs(flag2-flag1)>0.0001):
        flag2 -= np.divide(np.abs(flag1-flag2),values)
        flag1 += np.divide(np.abs(flag1-flag2),values)
    return flag1


f1 = 2
f2 = 5

x = np.linspace(start=1, stop=30.0, num=100)
y1 = FIRSTflagsandwich(values=x,flag1=f1,flag2=f2)
y2 = SECONDflagsandwich(values=x,flag1=f1,flag2=f2)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y1+y2)
plt.ylabel('Converged Number')
plt.xlabel('Divider')
plt.show()



