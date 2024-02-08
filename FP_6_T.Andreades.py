def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    for item in sorted_items:
        if total_cost + item[1]['cost'] <= budget:
            selected_items.append(item[0])
            total_cost += item[1]['cost']
    
    return selected_items

def dynamic_programming(items, budget):
    # Ініціалізуємо DP таблицю, де dp[i] буде максимальною калорійністю, яку можна отримати з бюджетом i
    dp = [0] * (budget + 1)
    
    # Зберігаємо набір страв, що використовуються для кожного бюджету
    item_sets = [[] for _ in range(budget + 1)]
    
    for i in range(1, budget + 1):
        for item, details in items.items():
            if details['cost'] <= i:
                # Якщо включення цієї страви дає більше калорій, ніж поточне максимальне значення для цього бюджету
                if dp[i - details['cost']] + details['calories'] > dp[i]:
                    dp[i] = dp[i - details['cost']] + details['calories']
                    # Оновлюємо набір страв для бюджету i
                    item_sets[i] = item_sets[i - details['cost']] + [item]
    
    return item_sets[budget]

# Вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Виконання алгоритмів
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

greedy_result, dynamic_result
