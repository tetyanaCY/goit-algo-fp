import numpy as np
import matplotlib.pyplot as plt

# Кількість кидків
num_throws = 1_000_000

# Генерація кидків
throws = np.random.randint(1, 7, size=(num_throws, 2))
sums = throws.sum(axis=1)

# Підрахунок результатів
sum_counts = np.bincount(sums)[2:]  # Індекси 0 та 1 не використовуються

# Обчислення імовірностей
probabilities = sum_counts / num_throws

# Відображення результатів
sums_range = np.arange(2, 13)  # Можливі суми

# Побудова таблиці
table_data = np.vstack((sums_range, probabilities * 100)).T

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.bar(sums_range, probabilities * 100, color='skyblue')
plt.xlabel('Сума')
plt.ylabel('Імовірність, %')
plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.xticks(sums_range)
plt.grid(axis='y', linestyle='--')

plt.show(), table_data
