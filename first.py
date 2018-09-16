import numpy as np
import matplotlib.pyplot as mlp
a,b,c=1,-1,-1
d1=(-b+np.sqrt(b**2-4*a*c))/2/a
d2=(-b-np.sqrt(b**2-4*a*c))/2/a
print(a*d1**2+b*d1+c);
print(a*d2**2+b*d2+c)