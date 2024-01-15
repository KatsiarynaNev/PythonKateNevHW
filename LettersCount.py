text = """
Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!
"""

# Приведем текст к нижнему регистру и удалим знаки препинания и пробелы
cleaned_text = ''.join(char.lower() for char in text if char.isalpha() or char.isspace())

# Подсчет частоты встречаемости букв
letter_count = {}
for char in cleaned_text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

# Подсчет встречаемости слова 'Python'
python_count = cleaned_text.split().count('python')

# Нахождение буквы с максимальной частотой
most_common_letter = max(letter_count, key=letter_count.get)

# Вывод результатов
print(f"Наиболее частая буква: {most_common_letter}, количество раз: {letter_count[most_common_letter]}")
print(f"Количество встреч слова 'Python': {python_count}")
