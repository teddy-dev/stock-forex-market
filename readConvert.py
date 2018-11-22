with open ('GBPUSD240.csv', 'r') as f:
    fl = f.readlines()
date, time, low, high, op, cl,  vol = [ [] for _ in range(7) ]
elem = [ date, time, low, high, op, cl,  vol ]
for _ in fl:
    string = _.split(',')
    [elem[i].append(string[i]) for i in range(len(elem))]
        
'''file structure:
2018.08.16,12:00,1.2703,1.2755,1.2697,1.2722,2021
  date            time     low    high    open   close  vol
    0                   1         2         3           4         5       6       :  всего 7
'''
print('I got it !!! ')

from mainMod import a
