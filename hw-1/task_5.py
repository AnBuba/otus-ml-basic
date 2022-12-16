
import numpy as np

# 5.1
my_array = np.random.randint(0, 2, size=100)
print('Ответ 5.1')
print(np.max(my_array), np.min(my_array))
print(my_array)

# 5.2
my_array = np.random.randint(0, 51, (5, 6))
# Находим максимальный элемент
# и столбец с максимальным значением (выведет последний, столбцов может быть несколько)
max = my_array[0][0]
for i in range(my_array.shape[0]):
    for j in range(my_array.shape[1]):
        if max < my_array[i][j]:
            max = my_array[i][j]
            a = j

selected_column = my_array[:,a]
print()
print('Ответ 5.2')
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)

# 5.3

def get_unique_rows(my_array):

    X_unique = np.array(my_array[0])
    list_str = [str(X_unique)]

    for i in range(1, my_array.shape[0]):
        b = np.array(my_array[i])
        if str(b) not in list_str:
            X_unique = np.vstack([X_unique, b])
            list_str.append(str(b))

    print(X_unique)

my_array = np.random.randint(4, 6, size=(10,3))
print()
print('Ответ 5.3')
print('array :')
print(my_array)
print('unique_rows :')
get_unique_rows(my_array)