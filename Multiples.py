def sum_multiples(limit):
    limit -= 1  # Исключаем само значение limit из ряда
    sum_of_threes = (3 * (limit // 3) * (limit // 3 + 1)) // 2
    sum_of_fives = (5 * (limit // 5) * (limit // 5 + 1)) // 2
    sum_of_fifteens = (15 * (limit // 15) * (limit // 15 + 1)) // 2
    total_sum = sum_of_threes + sum_of_fives - sum_of_fifteens
    return total_sum

# Пример использования
result = sum_multiples(100000000)
print(result)
