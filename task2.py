import math

print("Завдання 2: Табуляція функції за допомогою циклу WHILE")

a = float(input("Введіть початок діапазону (a): "))
b = float(input("Введіть кінець діапазону (b): "))
h = float(input("Введіть крок (h): "))

print("\nРезультати табуляції:")
print(f"{'x':<10} | {'f(x)':<10}")
print("-" * 25)

x = a
# Додаємо мале число (1e-9) для уникнення помилок округлення з float
while x <= b + 1e-9:
    if x >= 0:
        argument = abs(x + math.sqrt(x))
        if argument > 0:
            y = math.log10(argument)
            print(f"{x:<10.2f} | {y:<10.4f}")
        else:
            print(f"{x:<10.2f} | Помилка (lg(0))")
    else:
        print(f"{x:<10.2f} | Помилка (x < 0)")
    x += h
