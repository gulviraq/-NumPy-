import numpy as np

values = np.array([5, 10, 15, 20, 25])
print(values)


# Задание 2. 
zeros = np.zeros(5, dtype=int)
ones = np.ones(4, dtype=int)
even_numbers = np.arange(2, 13, 2)

print(zeros)
print(ones)
print(even_numbers)


# Задание 3.
a = np.array([[3, 6, 9],
              [12, 15, 18]])

print("ndim:", a.ndim)
print("shape:", a.shape)
print("size:", a.size)
print("dtype:", a.dtype)


# Задание 4. 
numbers = np.array([10, 20, 30, 40, 50])

print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])
print("Последний элемент:", numbers[-1])

numbers[2] = 100
print("После замены 30 на 100:", numbers)


# Задание 5. 
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# Задание 6. 
grades = np.array([[85, 90, 78],
                   [70, 88, 92],
                   [95, 81, 89]])

print("Оценка 88:", grades[1, 1])
print("Вторая строка:", grades[1, :])
print("Третий столбец:", grades[:, 2])
