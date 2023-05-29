from modifyingSVMFunctions import ModifyingSVM
from addWeightsFunctions import AddWeights

import numpy as np
import matplotlib.pyplot as plt
import math

### Data ###
batas_daerah_atas = [[1,38],[2,37],[3,36],[4,35],[5,34],[6,34],[7,35],[8,35],[9,34],[10,34],
               [11,33],[12,32],[13,31],[14,30],[15,29],[16,29],[17,28],[18,28],[19,27],[20,28],
               [21,29],[22,29],[23,29],[24,30],[25,29],[26,28],[27,29],[28,30],[29,30],[30,31],
               [31,32],[32,32],[33,33],[34,32],[35,31],[36,30],[37,29]]
batas_daerah_bawah = [[1,21],[2,20],[3,20],[4,19],[5,18],[6,18],[7,18],[8,18],[9,18],[10,17],
                [11,16],[12,15],[13,14],[14,14],[15,14],[16,13],[17,13],[18,12],[19,11],[20,10],
                [21,10],[22,9],[23,9],[24,8],[25,7],[26,7],[27,7],[28,6],[29,5],[30,4],
                [31,3],[32,3],[33,3],[34,3],[35,4],[36,5],[37,6]]

batas_daerah_atas = np.array([np.array([row[1], -1 * row[0]]) for row in batas_daerah_atas])
batas_daerah_bawah = np.array([np.array([row[1], -1 * row[0]]) for row in batas_daerah_bawah])

sda_bawah = [[[5, 12], [4, 12], [3, 13], [2, 14], [1, 15], [1, 16], [1, 17], [2, 17], [3, 16], [4, 16], [5, 16], [6, 15], [7, 15], [8, 14], [7, 13], [6, 12]],
             [[13, 12], [14, 12], [15, 12], [16, 11], [17, 11], [18, 10], [18, 9], [18, 8], [17, 7], [16, 7], [15, 8], [14, 9], [13, 10], [13, 11]]]
sda_atas = [[[15, 35], [16, 35], [17, 35], [18, 35], [18, 34], [18, 33], [18, 32], [17, 31], [16, 31], [15, 31], [14, 32], [13, 33], [14, 34]],
            [[21, 37], [22, 38], [23, 38], [24, 37], [25, 36], [25, 35], [24, 34], [23, 35], [22, 36]],
            [[31, 38], [32, 38], [33, 38], [34, 38], [35, 38], [36, 38], [36, 37], [36, 36], [35, 35], [34, 35], [33, 35], [32, 35], [31, 35], [30, 35], [29, 35], [29, 36], [30, 37]]]
sda_tengah = [[30, 7], [30, 6], [29, 6], [28, 7], [28, 8], [29, 8]]

sda_bawah = np.array([np.array([np.array([row[1], -1 * row[0]]) for row in sda]) for sda in sda_bawah])
sda_atas = np.array([np.array([np.array([row[1], -1 * row[0]]) for row in sda]) for sda in sda_atas])
sda_tengah = np.array([np.array([row[0], -1 * row[1]]) for row in sda_tengah])

pusat_sda_bawah = [[14, 5], [9, 16]] 
pusat_sda_atas = [[33, 16], [36, 23], [36, 33]]
pusat_sda_tengah = np.array([29, -7])

pusat_sda_bawah = np.array([np.array([row[0],  -1 * row[1]]) for row in pusat_sda_bawah])
pusat_sda_atas = np.array([np.array([row[0],  -1 * row[1]]) for row in pusat_sda_atas])

value_sda_bawah = np.array([90, 30])
value_sda_atas = np.array([30, 30, 30])
value_sda_tengah = np.array([30])

addweights = AddWeights(batas_daerah_atas, batas_daerah_bawah, 
                        pusat_sda_atas, pusat_sda_bawah, pusat_sda_tengah,
                        value_sda_atas, value_sda_bawah, value_sda_tengah)

data1_weighted, data2_weighted = addweights.geser_all_titik()
modifyingsvm = ModifyingSVM(batas_daerah_atas, batas_daerah_bawah)
peta_svm, domain_svm = modifyingsvm.garis_pembagi_wilayah()


plt.scatter(batas_daerah_atas[:, 0], batas_daerah_atas[:, 1])
plt.scatter(batas_daerah_bawah[:, 0], batas_daerah_bawah[:, 1])
plt.scatter(peta_svm, domain_svm)
for wp1 in sda_bawah:
    plt.scatter(wp1[:, 0], wp1[:, 1])
for wp2 in sda_atas:
    plt.scatter(wp2[:, 0], wp2[:, 1])
plt.scatter(sda_tengah[:, 0], sda_tengah[:, 1])
plt.legend(['Batas Daerah 1', 'Batas Daerah 2', 'Garis Pembagi Wilayah', 'Sumber Daya Alam Daerah 1', 'Sumber Daya Alam Daerah 2', 'Sumber Daya Alam Daerah 3'])

plt.show()