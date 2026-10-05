import math

print("Завдання 3: Обробка списку значень функції")

a = float(input("Введіть початок діапазону (a): "))
b = float(input("Введіть кінець діапазону (b): "))
h = float(input("Введіть крок (h): "))

f_values = []  # Порожній список для значень функції
x_values = []  # Список для відповідних значень x (щоб бачити їх у виведенні)

x = a
while x <= b + 1e-9:
    if x >= 0:
        argument = abs(x + math.sqrt(x))
        if argument > 0:
            y = math.log10(argument)
            f_values.append(y)
            x_values.append(x)
    x += h

# 1. Виведення списку в рядок
print("\nОтриманий список значень f(x):")
print([round(val, 4) for val in f_values])

# 2. Визначення індексів найбільшого та найменшого елементів
if f_values:
    max_value = max(f_values)
    min_value = min(f_values)
    
    max_index = f_values.index(max_value)
    min_index = f_values.index(min_value)
    
    print(f"\nМаксимальне значення: {max_value:.4f} (індекс: {max_index}, при x = {x_values[max_index]:.2f})")
    print(f"Мінімальне значення: {min_value:.4f} (індекс: {min_index}, при x = {x_values[min_index]:.2f})")
else:
    print("\nСписок порожній. Перевірте введені межі діапазону!")
