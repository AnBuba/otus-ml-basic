import numpy as np
import scipy.spatial.distance as ds

def cal_euclidean(a, b):
    sq = np.square(a - b)
    sum_sq = np.sum(sq)
    distance = np.sqrt(sum_sq)
    return distance

def cal_manhattan(a, b):
    a = abs(a - b)
    distance = np.sum(a)
    return distance

def cal_cosine(a, b):
    distance = ds.cosine(a, b)
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(f'a = {a}')
print(f'b = {b}')
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))