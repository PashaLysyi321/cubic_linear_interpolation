import math 
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = [1.9,5.2,9.8,17.3,25.7,37.5]
numm = 6
n = len(x)
sumXY = sumX = sumY = sumX2 = 0


for i in range(0,n):
	
	sumXY = sumXY+ x[i]*y[i]
	sumX = sumX + x[i]
	sumY = sumY + y[i]
	sumX2 = sumX2 + x[i]*x[i]

a = (n*sumXY-sumX*sumY)/(n*sumX2-sumX*sumX)
b = (sumY-a*sumX)/n


print('linear polynom is: '+str(a)+'x'+' '+ str(b))
xx = [x[0],numm]
yy = []

for i in xx:
	yy.append(a*i+b)

ans = a*numm+b
print('answer in x0=6 is: ' + str(ans))

#linx =[] #значения в х по lm
#for i in x:
#	linx.append(a*i+b)
#for i in x:
#	print(math.fabs(linx[i]-y[i]))

plt.plot(xx,yy, color = 'blue',label = 'linear approximation')
plt.scatter(x,y, color = 'red',label = 'True points')
plt.scatter(numm,ans,color = 'green', label = 'Predicted point')
plt.title(' linear approximation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'lower right')
plt.yticks([0,5,10,15,20,25,30,35,40,45])
plt.xticks([0,1,2,3,4,5,6])
plt.grid()
plt.show()
