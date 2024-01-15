numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

# Преобразование элементов в тип int() с обработкой ошибок и фильтрацией
int_numbers = []
for item in numbers:
    if isinstance(item, (int, float)):
        int_numbers.append(item)
    elif isinstance(item, str) and item.replace('.', '').lstrip('-').isdigit():
        # Если строка состоит только из цифр, включая отрицательные числа и числа с плавающей точкой
        int_numbers.append(float(item))

# Исключение значений None, так как float(None) вызывает TypeError
int_numbers = [item for item in int_numbers if item is not None]

if int_numbers:
    min_value = min(int_numbers)
    max_value = max(int_numbers)

    print("Минимальное значение:", min_value)
    print("Максимальное значение:", max_value)
else:
    print("Список не содержит подходящих элементов для нахождения минимального и максимального значения.")
