import turtle
import math

# Функція для малювання квадрата
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

# Рекурсивна функція для створення дерева Піфагора
def draw_pythagoras_tree(t, size, level):
    if level == 0:
        draw_square(t, size)
        return

    # Малюємо основний квадрат
    draw_square(t, size)

    # Підготовка до рекурсивного малювання гілок
    t.forward(size)
    t.left(45)

    # Малювання лівої гілки
    draw_pythagoras_tree(t, size * math.sqrt(2) / 2, level - 1)

    # Переміщення до позиції для правої гілки
    t.right(90)
    t.forward(size * math.sqrt(2))

    # Малювання правої гілки
    draw_pythagoras_tree(t, size * math.sqrt(2) / 2, level - 1)

    # Повернення до початкової позиції
    t.backward(size * math.sqrt(2))
    t.left(45)
    t.backward(size)

# Налаштування та створення вікна
window = turtle.Screen()
window.title("Дерево Піфагора")

# Створення об'єкту turtle
t = turtle.Turtle()
t.speed('fastest') # найшвидша швидкість малювання

# Початкова позиція
t.up()
t.goto(0, -200)
t.down()

# Встановлюємо рівень рекурсії
recursion_level = 5 # Змініть це значення, щоб вказати рівень рекурсії

# Малюємо дерево
draw_pythagoras_tree(t, 80, recursion_level)

# Завершення роботи
window.mainloop()
