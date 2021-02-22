from triclass import triangle
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    
    #matplotlib
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    #point definition
    p={}
    p['x'] = 2
    p['y'] = 3
    p['z'] = 4
    #triangle definition
    pos1 = {'x':-5,'y':5,'z':0}
    pos2 = {'x':5,'y':-5,'z':0}
    pos3 = {'x':5,'y':5,'z':-1}
    x = pos1['x'], pos2['x'], pos3['x']
    y = pos1['y'], pos2['y'], pos3['y']
    z = pos1['z'], pos2['z'], pos3['z']

    a = pos1['y'] * (pos2['z'] - pos3['z']) + pos2['y'] * (pos3['z'] - pos1['z']) + pos3['y'] * (pos1['z'] - pos2['z'])
    b = pos1['z'] * (pos2['x'] - pos3['x']) + pos2['z'] * (pos3['x'] - pos1['x']) + pos3['z'] * (pos1['x'] - pos2['x'])
    c = pos1['x'] * (pos2['y'] - pos3['y']) + pos2['x'] * (pos3['y'] - pos1['y']) + pos3['x'] * (pos1['y'] - pos2['y'])
    d = (pos1['x'] * (pos2['y'] * pos3['z'] - pos3['y'] * pos2['z']) + 
        pos2['x'] * (pos3['y'] * pos1['z'] - pos1['y'] * pos3['z']) + 
        pos3['x'] * (pos1['y'] * pos2['z'] - pos2['y'] * pos1['z']))

    print(a,b,c, d)
    dist_plane = abs(a * p['x'] + b * p['y'] + c * p['z'] + d) / math.sqrt(a * a + b * b + c * c)
    print("Distance point plan :", dist_plane)
    
    # Matplotlib
    ax.scatter(p['x'], p['y'], p['z'], color="r")
    verts = [list(zip(x, y, z))]
    print(verts)
    ax.add_collection3d(Poly3DCollection(verts))
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    
    plt.show()

if __name__ == '__main__':
    main()

    