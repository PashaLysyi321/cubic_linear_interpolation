import math 
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = [1.9,5.2,9.8,17.3,25.7,37.5]
numm = 6
n = len(x)

print('binomial polynom is: y = 1.0304*x^2+1.9054*x+2.0250')

xx=[]
yy=[]

for i in range (0,600):
	xx.append(i/100)
	yy.append(1.0304*i*i/10000+1.9054*i/100+2.0250)
	
ans = 1.0304*numm*numm+1.9054*numm+2.0250

print('answer in x0=6 is: ' + str(ans))

#linx =[] #значения в х по lm
#for i in x:
#	linx.append(1.0304*i*i+1.9054*i+2.0250)
#for i in x:
#	print(math.fabs(linx[i]-y[i]))

plt.scatter(xx,yy, color = 'blue',label = 'quadratic approximation',s = 1)
plt.scatter(x,y, color = 'red',label = 'True points')
plt.scatter(numm,ans,color = 'green', label = 'Predicted point')
plt.title('quadratic approximation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'lower right')
plt.yticks([0,5,10,15,20,25,30,35,40,45,50])
plt.xticks([0,1,2,3,4,5,6])
plt.grid()
plt.show()
