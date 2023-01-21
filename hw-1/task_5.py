import numpy as np

# 5.1
my_array = np.random.rand(100)
my_array[my_array.argmax()] = 1
my_array[my_array.argmin()] = 0

print('Ответ 5.1')
print(np.max(my_array), np.min(my_array))
print(my_array)

# 5.2
my_array = np.random.randint(0, 51, (5, 6))
selected_column = my_array[:, np.argmax(my_array.max(axis=0))]
print()
print('Ответ 5.2')
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)

# 5.3

def get_unique_rows(my_array):
    X_unique = np.unique(my_array, axis=0)
    print(X_unique)

my_array = np.random.randint(4, 6, size=(10,3))
print()
print('Ответ 5.3')
print('array :')
print(my_array)
print('unique_rows :')
get_unique_rows(my_array)