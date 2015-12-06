import matplotlib.pyplot as plt
from ast import literal_eval
grid = []
with open("grid.txt") as f:
    for line in f:
        grid.insert(0,literal_eval(line[:-1]))

m = len(grid)
n = len(grid[0])

ax = plt.gca()
ax.xaxis.set_ticks(range(1,n+1))
ax.yaxis.set_ticks(range(1,m+1))
# create a grid
ax.grid(True, linestyle='-', linewidth=1)
# put the grid below other plot elements
ax.set_axisbelow(True)

for i in range(m):
    for j in range(n):
        walls = grid[i][j][0]
        flag = grid[i][j][1]
        if walls & 1:
            ax.axvline(x=j,ymin=float(i)/m,ymax=float(i+1)/m,linewidth=4, color='k')
        if walls & 2:
            ax.axhline(y=i,xmin=float(j)/n,xmax=float(j+1)/n,linewidth=4, color='k')
        if flag:
            ax.text(float(j+0.5)/n, float(i+0.5)/m, flag, fontsize=12,horizontalalignment='center',
                    verticalalignment='center',
                    transform=ax.transAxes)
ax.axhline(y=m,linewidth=4,color='k')
ax.axvline(x=n,linewidth=4,color='k')
plt.draw()

plt.show()