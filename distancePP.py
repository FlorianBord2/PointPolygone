import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

def display(A,B,C,P):
    #config matplotlib
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    #draw triangle
    x = A[0], B[0], C[0]
    y = A[1], B[1], C[1]
    z = A[2], B[2], C[2]
    verts = [list(zip(x, y, z))]
    ax.add_collection3d(Poly3DCollection(verts))
    #draw text
    ax.scatter(P[0], P[1], P[2], color="r")
    ax.text(P[0], P[1], P[2], "P",color="g")
    ax.text(A[0], A[1], A[2], "A", color="r")
    ax.text(B[0], B[1], B[2], "B", color="r")
    ax.text(C[0], C[1], C[2], "C", color="r")
    text = "AP = " + calcul_distance(A, P) + "\nBP = " + calcul_distance(B, P) + "\nCP = " + calcul_distance(C,P)
    ax.text2D(0.0, 0.0, text, transform=ax.transAxes)
    plt.show()

def calcul_distance(position, point):
    position = np.array([position[0], position[1], position[2]])
    point = np.array([point[0], point[1], point[2]])
    squared_dist = np.sum((point-position)**2, axis=0)
    dist = np.sqrt(squared_dist)
    return(str(dist))

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "-m":
            first_point = input("Give me your 'A' triangle point like 'x,y,z'\n")
            second_point = input("Now your 'B' triangle point like 'x,y,z'\n")
            third_point = input("And then 'C' point like 'x,y,z'\n")
            point = input("And finnaly give me your 'D' point, the one outside the triangle, like 'x,y,z'\n")
            A = [float(x) for x in first_point.split(',')]
            B = [float(x) for x in second_point.split(',')]
            C = [float(x) for x in third_point.split(',')]
            P = [float(x) for x in point.split(',')]
    else:
        A = [4, 2, 1]
        B = [-3, 2, -3]
        C = [-4, 4, 1]
        P = [4 , -3, 1]
    display(A,B,C,P)

if __name__ == '__main__':
    main()
