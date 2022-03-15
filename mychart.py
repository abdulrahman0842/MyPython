import pandas as p
import matplotlib.pyplot as m
import pylab

readexcel = p.read_excel('C:\\Users\\pc\\Desktop\\rkbhu.xlsx')
print(readexcel.head())
m.plot(readexcel['Column01'])
