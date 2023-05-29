from modifyingSVMFunctions import ModifyingSVM
from addWeightsFunctions import AddWeights

import numpy as np
import matplotlib.pyplot as plt
import math

### Dataset 1 ###
# y1 = np.arange(0, 10, 0.025)
# x1 = np.zeros(len(y1)) + 5
# data1 = np.array([x1, y1]).T
# y2 = np.arange(0, 10, 0.025)
# x2 = np.zeros(len(y1)) + 15
# data2 = np.array([x2, y2]).T

# weight_points1 = np.array([np.array([-3, 5]), np.array([4, 0])]) 
# weight_points2 = np.array([np.array([17, 3]), np.array([20, 0]), np.array([16, 10])])
# weight_points3 = np.array([[13, 5]])

# weight_values1 = np.array([55, 90])
# weight_values2 = np.array([60, 70, 35])
# weight_values3 = np.array([70])

# weight_radius1 = np.array([0.3, 0.3])
# weight_radius2 = np.array([0.3, 0.3, 0.3])
# weight_radius3 = np.array([0.3])
### Dataset 1 ###

### Dataset 2 ###
y1 = np.arange(-10, 10, 0.01)
x1 = np.sin(y1) 
data1 = np.array([x1, y1]).T
y2 = np.arange(-10, 10, 0.01)
x2 = np.abs(np.sin(y2)) + 5
data2 = np.array([x2, y2]).T

weight_points1 = np.array([np.array([0, 1.25]), np.array([-2, -1.25])])
weight_points2 = np.array([np.array([7, -5]), np.array([7, 0]), np.array([7, 7.5])])
weight_points3 = np.array([np.array([4, 5]), np.array([1.5, -7])])

weight_values1 = np.array([55, 90])
weight_values2 = np.array([60, 70, 35])
weight_values3 = np.array([70, 75])

weight_radius1 = np.array([0.3, 0.3])
weight_radius2 = np.array([0.3, 0.3, 0.3])
weight_radius3 = np.array([0.3, 0.3])
### Dataset 2 ###

def create_circle(point, r):
    n = 1000
    pi = math.pi
    circle = np.array([np.array([math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r]) for x in range(0,n+1)])
    circle = np.array([np.array([coor[0] + point[0], coor[1] + point[1] ]) for coor in circle]) 
    return circle

def generate_all_circle():
    weight_plot1 = [create_circle(point, r) for point, r in zip(weight_points1, weight_radius1)]
    weight_plot2 = [create_circle(point, r) for point, r in zip(weight_points2, weight_radius2)]
    weight_plot3 = [create_circle(point, r) for point, r in zip(weight_points3, weight_radius3)]
    return (weight_plot1, weight_plot2, weight_plot3)

weight_plot1, weight_plot2, weight_plot3 = generate_all_circle()

### Menggunakan fungsi yang telah dibuat untuk mencari garis pembatas wilayah
addweights = AddWeights(data1, data2, 
                        weight_points1, weight_points2, weight_points3, 
                        weight_values1, weight_values2, weight_values3)
data1_weighted, data2_weighted = addweights.geser_all_titik()
modifyingsvm = ModifyingSVM(data1_weighted, data2_weighted)
peta_svm, domain_svm = modifyingsvm.garis_pembagi_wilayah()

### Memvisualisasikan data 1, data 2, garis pembagi wilayah, serta sumber daya alam
plt.scatter(data1[:,0], data1[:,1])
plt.scatter(data2[:,0], data2[:,1])
# plt.scatter(data1_weighted[:,0], data1_weighted[:,1], alpha=0.1)
# plt.scatter(data2_weighted[:,0], data2_weighted[:,1], alpha=0.1)
plt.scatter(peta_svm, domain_svm)
for wp1 in weight_plot1:
    plt.scatter(wp1[:, 0], wp1[:, 1])
for wp2 in weight_plot2:
    plt.scatter(wp2[:, 0], wp2[:, 1])
for wp3 in weight_plot3:
    plt.scatter(wp3[:, 0], wp3[:, 1])

plt.legend(['Batas Daerah 1', 'Batas Daerah 2'])

plt.show()
