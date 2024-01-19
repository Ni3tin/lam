
# a = 2
# b= 3
# x = map(lambda a,b : a*b ,[3,5])
# print(x)

# N_list=[2,5,7,8,11,12,20]
# n= list(filter(lambda a : (a/2==4),N_list))
# print(n)
# n1 = list(map(lambda a : (a+4),N_list))
# print(n1)
# from functools import reduce
# n2= reduce(lambda a,b : a+b,[2,4,6,8])
# print(n2)
# c = map(lambda v : (v+2),(2,3,5,9))
# print(list(c))
# c1 = filter(lambda v : (v>2),(2,3,5,9))
# print(list(c1))
# from functools import reduce
# c2 = reduce(lambda v,w : (v*w),[3,2,6,4])
# print(c2)
# from functools import reduce
# z = map(lambda s : s-2, filter(lambda d : d>14,[12,21,31,42,44,51]))
# print(list(z))
# z1 = filter(lambda s : s>49, map(lambda d : d+12,[12,21,31,42,44,51]))
# print(tuple(z1))
# z2 = reduce(lambda b,n :b+n,(map(lambda s : s-2, filter(lambda d : d>14,[12,21,31,42,44,51]))))
# print(z2)
# z3 = reduce(lambda b,n :b+n,(filter(lambda s : s>49, map(lambda d : d+12,[12,21,31,42,44,51]))))
# print(z3)

# import time
# print(time.time())
# print(time.ctime())
# print(time.localtime())
# d =time.localtime()
# print(time.asctime(d))

# import datetime
# print(datetime.time())
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# r = datetime.datetime.now()
# print(r.day)
# print(r.month)
# print(r.year)

from statistics import mean
print(mean([3,4,5,6,1,2,7]))
from statistics import mode
print(mode([3,4,5,6,1,2,5]))
from statistics import median
print(median([3,4,5,6,1,2,7]))



