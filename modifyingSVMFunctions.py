from warnings import simplefilter

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True, figsize=(7, 7))

simplefilter("ignore")

class ModifyingSVM:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def _gradien_titik_terluar(self, data):
        """Menentukan gradien garis singgung untuk setiap 2 titik yang berdekatan pada dataset"""
        d1 = data[:-1]
        d2 = data[1:]
        return (d1[:,1] - d2[:,1]) / (d1[:,0] - d2[:,0])

    def _data_per_segmen(self, data):
        """Melakukan segementasi untuk seluruh titik pada dataset dengan meninjau perubahan gradien garis singgung"""
        gradien_data = self._gradien_titik_terluar(data)
        segmen = []
        n = 1
        j = 0
        for i in range(len(gradien_data) - 1):
            temp_grad = [np.abs(gradien_data[j]), np.abs(gradien_data[i+1])]
            min_grad = np.min(temp_grad)
            max_grad = np.max(temp_grad)
            gradien_change = min_grad / max_grad
            if not ((gradien_change > 0.999 and gradien_data[j] * gradien_data[i+1] > 0) or np.isnan(gradien_change)):
                n += 1
                j = i
            segmen.append(n)
        return np.array(segmen)

    def _indexes_per_segmen(self):
        """Memberikan range index untuk masing-masing segmen"""
        data1 = self._data_per_segmen(self.data1)
        data2 = self._data_per_segmen(self.data2)
        indexes_ = []
        for i in range(len(data1) - 1):
            if data1[i] != data1[i+1]:
                indexes_.append(i+1)
            if data2[i] != data2[i+1]:
                indexes_.append(i+1)
        indexes_.append(len(data1))
        indexes = np.sort(np.unique(np.array(indexes_)))
        return indexes

    def _seperate_data_into_segmen(self):
        """Membentuk sebuah dataset yang memuat titik-titik dari masing-masing segmen"""
        indexes = self._indexes_per_segmen()
        data = []
        start = 0
        for stop in indexes:
            d1 = self.data1[start:stop]
            d2 = self.data2[start:stop]
            d = np.concatenate((d1, d2))
            data.append(d)
            start = stop   
        return np.array(data)
    
    def _fungsi_garis_svm(self, sample, clf_):
        """Membentuk garis pembagi wilayah menggunakan hasil fitting SVM linear"""
        koef = - clf_.coef_[0, 1] / clf_.coef_[0, 0]
        intercept = - clf_.intercept_[0] / clf_.coef_[0, 0]
        return sample * koef + intercept       

    def garis_pembagi_wilayah(self):
        """Eksekusi pembentukan garis pembagi wilayah dari kedua dataset"""
        data = self._seperate_data_into_segmen()
        domain_svm = []
        peta_svm = []
        for d in data:
            clf = svm.SVC(kernel='linear')
            X = d 
            y = [1 if i <= int(len(d)/2) else 2 for i in range(1, len(d)+1)] 
            clf.fit(X, y)
            samples = d[:int(len(d)/2),1]
            for sample in samples:
                peta_svm.append(self._fungsi_garis_svm(sample, clf))
                domain_svm.append(sample)
        return (peta_svm, domain_svm)

