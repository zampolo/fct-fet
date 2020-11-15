import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,num=1e4)
f = (15/256)+(1/2)*x+(210/256)*(x**2) - (105/256)*(x**4)

plt.figure()
plt.plot(x,f,'r')
plt.grid(True)
plt.show()
