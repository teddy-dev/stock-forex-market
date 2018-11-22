import numpy as np
import matplotlib.pyplot as plt 
#import matplotlib.pylab as plt # работают оба эти варианта

x=np.arange(2,11,2)
y = x.copy()

fig, ax = plt.subplots()
ax.plot(x,y)

'''так мы через пайплот можем заменить ,
а точнее сопоставить текстовые значения х_лбл
по оси х с количеством значений по оси х.
'''
ax.set_xticks(x)
x_lbl = ['q','w','e','r','t']
ax.set_xticklabels(x_lbl)

fig.tight_layout()
plt.show()

