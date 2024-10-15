import matplotlib
import matplotlib.pyplot as plt

input_vlaues = [1,2,3,4,5]
cubes = [1,8,27,64,125]
plt.scatter(input_vlaues,cubes,edgecolor='none',s=40)
plt.title('Cubes',fontsize=24)
plt.xlabel('vlaue',fontsize=14)
plt.ylabel('cube of vlaue',fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()
