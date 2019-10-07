import math 
import matplotlib.pyplot as plt
import numpy as np

print('----------------Create by Lysyi Pavlo KM-71--------------') 
print('----------------This programm for cubic interpolation and linear interpolation-------------') 

x = [ -5, -3, -1, 1]
y = [ 2, 1, 3, 7]
s1 = 2
s2 = 3

print('input vales:'+'\n'+'x:'+str(x)+'\n'+'y:'+str(y)+'\n'+'s1:'+str(s1)+'\n'+'s2:'+str(s2))
diff = x[1]-x[0]

len = len(x)
h = [0]*(len-1)
d = [0]*(len-1)

for i in range(0,len-1):
	h[i] = x[i+1]-x[i]
	d[i] = (y[i+1]-y[i])/h[i]
#ищем матрицу
matrix = [[0]*(len)]*(len)
matrix[0] = [2,1,0,0]
matrix[1] = [h[0],2*(h[0]+h[1]),h[1],0]
matrix[2] = [0,h[1],2*(h[1]+h[2]),h[2]]
matrix[3] = [0,0,1,2]


v = [3/h[0]*(d[0]-s1)*2, 6*(d[1]-d[0]), 6*(d[2]-d[1]), 3/h[len-2]*(-d[len-2]+s2)*2]
print('Matrix + solution')
print(matrix)
print(v)
#решаем слау
M = np.array([matrix[0],matrix[1],matrix[2],matrix[3]])
v = np.array(v)
out = np.linalg.solve(M,v)
print('solution')
print(out)
#ищем a b c d
am = []
bm = []
cm = []
dm = []

for i in range(0,3):
	am.append(float(y[i]))
	bm.append(round(d[i]-h[i]*(2*out[i]+out[i+1])/6,4))
	cm.append(round(out[i]/2,4))
	dm.append(round((out[i+1]-out[i])/(6*h[i]),4))
print('The a b c d :')
print(am)
print(bm)
print(cm)
print(dm)


def func (num,i):
	fr = am[i]+bm[i]*(num-x[i])+cm[i]*(num-x[i])*(num-x[i])+dm[i]*(num-x[i])*(num-x[i])*(num-x[i])
	return fr

# рисуем график
xlist = []
ylist = []
for i in range(x[0]*100,x[1]*100,1):
    xlist.append(i/100)
    ylist.append(func(i/100,0))
for i in range(x[1]*100,x[2]*100,1):
    xlist.append(i/100)
    ylist.append(func(i/100,1))
for i in range(x[2]*100,x[3]*100,1):
    xlist.append(i/100)  
    ylist.append(func(i/100,2))

plt.plot (xlist, ylist, label = 'cubic polynomials')
plt.plot(x,y, color = 'red', label = 'linear polynomials')
plt.title(' Interpolations by cubic/linear polynomials')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'lower right')
plt.scatter(x,y)
plt.grid()
plt.show()