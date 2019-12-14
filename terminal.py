import matplotlib.pylab as plt
import numpy as np
##x = [1,1,1,1,
##     2,2,2,2,
##     3,3,3,3,
##     4,4,4,4 ]
##y = [10,5,25,15,
##     30,15,35,33,
##     26,11,37,31,
##     15,7,24,19 ]
with open ('GBPUSD240.csv', 'r') as f:
    fl = f.readlines()
date, time, op, high, low, cl,  vol = [[] for _ in range(7)]
elem = [date, time, op, high, low, cl,  vol]
for _ in fl:
    string = _.split(',')
    [elem[i].append(string[i]) for i in range(len(elem))]
        
'''file structure:
2018.08.16,12:00,1.2703,1.2755,1.2697,1.2722,2021
  date            time     open    high    low     close   vol
    0                   1         2         3           4         5       6       :  всего 7
'''
x = range(len(date))
y = [ [ min( op[i],cl[i] ), high[i], low[i], max(op[i], cl[i]) ] for i in x ]
#y = [ [high[i], low[i] ] for i in x ]

fig, ax = plt.subplots()
plt.plot(x, y)

plt.xlabel('date: days')
plt.ylabel('price')
plt.title('Фунт-доллар 4h')

#------------
'''так мы через пайплот (и через пайлаб) можем заменить ,
а точнее сопоставить текстовые значения х_лбл
по оси х с количеством значений по оси х.
'''
ax.set_xticks(x) # plt.xticks(x) аналогично

n_date= []
for _ in range(len(time)):
    n_date.append(date[_]+' - '+ time[_])
x_lbl = n_date.copy()

ax.set_xticklabels(x_lbl, rotation = 'vertical')  # только так, через пайплот не работает

'''
https://proglib.io/p/neural-nets-guide/
еще про текстовые метки 3 варианта
https://stackoverrun.com/ru/q/1932802
'''
#----------------------------------Moving average--------------

p=7
ln = len(cl)
wa = lambda x : round(sum(x)/len(x), 4)
beg = 0
end = p
ma = [None for x in range(p)] ; print(ma)
for i in range(ln-p):
    ma.append(wa( list(map(float, cl[ beg: end]))))
    beg += 1
    end += 1

plt.plot(x, ma)

fig.tight_layout()
plt.show()
print(
'''Выводы на будущее:
окно сделать со скроллами, или пока уменьшить диапазон'''
)
input('press enter..')
    
    
    
