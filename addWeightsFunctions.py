from warnings import simplefilter

import numpy as np
import math

simplefilter("ignore")

class AddWeights:
    def __init__(self, data1, data2, weight_points1, weight_points2, weight_points3, 
                                        weight_values1, weight_values2, weight_values3):
        self.data1, self.data2 = data1, data2
        self.weight_points1, self.weight_points2, self.weight_points3 = weight_points1, weight_points2, weight_points3
        self.weight_values1, self.weight_values2, self.weight_values3 = weight_values1, weight_values2, weight_values3

    def _max_pergeseran(self):
        """Menentukan panjang pergerseran maksimal suatu titik terluar yaitu setengah dari jarak 2 titik terluar yang berada pada koordinat y yang sama"""
        jarak_tengah = (self.data1 + self.data2) / 2
        max_pergeseran = jarak_tengah.T[0]/2
        return max_pergeseran   

    def _distance_from_point_to_weight(self, weightp, data, position):
        """Menentukan jarak antara sumber daya alam dengan titik terluar"""
        if position == 'left':
            distance = weightp - data
        else:
            distance = data - weightp
        distance = np.sum(distance * distance, axis=1)**0.5
        return distance

    def _max_weight_value(self):
        """Menentukan bobot sumber daya alam yang terbesar"""
        weight_values = np.concatenate((self.weight_values1, self.weight_values2))
        max_weight_val = np.max(weight_values)
        return max_weight_val
    
    def _geser_titik(self, max_pergeseran, distance, max_weight_val, weight_val, data, position):
        """Menggeser seluruh titik terluar terhadap sebuah sumber daya alam"""
        calc = (max_pergeseran / distance) * (weight_val / max_weight_val)
        if position == 'left':
            data = np.array([data[:, 0] - calc, data[:, 1]]).T
        else:
            data = np.array([data[:, 0] + calc, data[:, 1]]).T
        return data

    def geser_all_titik(self):
        """Menggeser seluruh titik terluar terhadap sumber daya alam"""
        max_pergeseran = self._max_pergeseran()
        max_weight_val = self._max_weight_value()
        for wp, wv in zip(self.weight_points1, self.weight_values1):
            distance = self._distance_from_point_to_weight(wp, self.data1, 'left')
            self.data1 = self._geser_titik(max_pergeseran, distance, max_weight_val, wv, self.data1, 'left')

        for wp, wv in zip(self.weight_points2, self.weight_values2):
            distance = self._distance_from_point_to_weight(wp, self.data2, 'right')
            self.data2 = self._geser_titik(max_pergeseran, distance, max_weight_val, wv, self.data2, 'right')

        for wp, wv in zip(self.weight_points3, self.weight_values3):
            distance_right = self._distance_from_point_to_weight(wp, self.data1, 'left')
            self.data1 = self._geser_titik(max_pergeseran, distance_right, max_weight_val, wv, self.data1, 'left')

            distance_left = self._distance_from_point_to_weight(wp, self.data2, 'right')
            self.data2 = self._geser_titik(max_pergeseran, distance_left, max_weight_val, wv, self.data2, 'right')
        
        return (self.data1, self.data2)
    
