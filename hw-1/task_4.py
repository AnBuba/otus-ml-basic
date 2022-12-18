import numpy as np

def cal_euclidean(a, b):
    sq = np.square(a - b)
    sum_sq = np.sum(sq)
    distance = np.sqrt(sum_sq)
    return distance

def cal_manhattan(a, b):
    a = np.abs(a - b)
    distance = np.sum(a)
    return distance

def cal_cosine(a, b):
    n1 = np.dot(a, b)
    a_1 = np.sqrt(np.sum(np.square(a)))
    b_1 = np.sqrt(np.sum(np.square(b)))
    distance = 1.0 - (n1 / (a_1 * b_1))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(f'a = {a}')
print(f'b = {b}')
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))