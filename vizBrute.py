# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from main import *

fig = plt.figure()
pointHasilColor = 'red'
pointHasilColorB = 'yellow'
pointsColor = 'blue'
lineHasilColor = 'green'
lineHasilColorB = 'yellow'
lineWidthConts = 2
# syntax for 3-D projection
if (dimension == 3):
    ax = plt.axes(projection =str(dimension)+'d') 
    ax.invert_yaxis()
    Stest = np.array([[0,0,0],[3,1,0],[3,3,4],[4,3,0]])
    # defining all 3 axis
    # x = Stest[:,0]
    # y = Stest[:,1]
    # z = Stest[:,2]
    x = List_Points[:,0]
    y = List_Points[:,1]
    z = List_Points[:,2]
    # xb = List_PointsBruteForce[:,0]
    # yb = List_PointsBruteForce[:,1]
    # zb = List_PointsBruteForce[:,2]
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)
    print (Phasil)
    xhasil = Phasil[:,0]
    yhasil = Phasil[:,1]
    zhasil = Phasil[:,2]
    xhasilB = PhasilBrute[:,0]
    yhasilB = PhasilBrute[:,1]
    zhasilB = PhasilBrute[:,2]
    # plt.invert_yaxis()
    # x = np.linspace(0, 1, 5)
    # y = np.linspace(0, 1, 9)
    # z = np.linspace(0, 1, 3)
    # print(x, y, z)
    # x = 1
    # y = 1
    # z = 1

    # plotting
    ax.plot3D(xhasil, yhasil, zhasil, lineHasilColor, linewidth = lineWidthConts)
    ax.plot3D(xhasil, yhasil, zhasil, lineHasilColorB, linewidth = lineWidthConts)
    # make points
    ax.scatter3D( x, y, z, color = pointsColor)
    ax.scatter3D( xhasil, yhasil, zhasil, color = pointHasilColor)
    ax.scatter3D( xhasil, yhasil, zhasil, color = pointHasilColorB)
    ax.set_title('3D line plot geeks for geeks')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()
    
elif(dimension == 2 ):
    # ax = plt.figure()
    # defining all 3 axis
    x = List_Points[:,0]
    y = List_Points[:,1]
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)
    print (Phasil)
    xhasil = Phasil[:,0]
    yhasil = Phasil[:,1]
    xhasilB = PhasilBrute[:,0]
    yhasilB = PhasilBrute[:,1]
    # print(x, y)
    
    # plotting
    plt.plot(xhasil, yhasil, lineHasilColor, linewidth = lineWidthConts)
    plt.plot(xhasilB, yhasilB, lineHasilColorB, linewidth = lineWidthConts)
    # make points
    plt.scatter( x, y, color = pointsColor)
    plt.scatter( xhasil, yhasil, color = pointHasilColor)
    plt.scatter( xhasilB, yhasilB, color = pointHasilColorB)
    plt.title('2D line plot geeks for geeks')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
elif (dimension == 1):
    # ax = plt.figure()
    # defining all 3 axis
    x = List_Points[:,0]
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)
    print (Phasil)
    xhasil = Phasil[:,0]
    xhasilB = PhasilBrute[:,0]
    # print(x, y)
    
    # plotting
    plt.plot(xhasil, lineHasilColor, linewidth = lineWidthConts)
    plt.plot(xhasilB, lineHasilColorB, linewidth = lineWidthConts)
    # make points
    plt.scatter( x, color = pointsColor)
    plt.scatter( xhasil, color = pointHasilColor)
    plt.scatter( xhasilB, color = pointHasilColorB)
    plt.title('1D line plot geeks for geeks')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
else :
    print('Error plotting, dimension not supported')
    