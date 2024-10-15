import matplotlib
import matplotlib.pyplot as plt
x_vlaues = list(range(5001))
y_values=[x**3  for x in x_vlaues ]
plt.scatter(x_vlaues, y_values, edgecolors='none', c=y_values, cmap=plt.cm.Blues, vmin=min(y_values), vmax=max(y_values), s=40)
plt.title("Cubes", fontsize=24)
plt.xlabel('value',fontsize='14')
plt.ylabel('Square value',fontsize='14')
plt.tick_params(axis='both',labelsize=14)
plt.axis([0,5100,0,5100**3])


plt.show()
