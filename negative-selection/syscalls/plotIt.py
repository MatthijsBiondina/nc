from matplotlib import pyplot as plt
import sys
scores = open('scores.txt','r').read()

data = scores.split()
float_data = [float(d) for d in data]
r = range(1,10)

title = sys.argv[1]

plt.plot(r,float_data)
plt.xlabel("r")
plt.ylabel('AUC')
plt.title(title)
plt.show()
