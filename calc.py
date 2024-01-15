def file_size(size_in_bytes):
    suffixes = ['B', 'KB', 'MB', 'GB']
    index = 0
    size = float(size_in_bytes)

    while size > 1024 and index < len(suffixes) - 1:
        size /= 1024.0
        index += 1

    return '{:.1f}{}'.format(size, suffixes[index])

# Примеры использования
print(file_size(19))        # '19.0B'
print(file_size(12345))     # '12.1KB'
print(file_size(1101947))   # '1.1MB'
print(file_size(572090))    # '558.7KB'
print(file_size(999999999999))  # '931.3GB'
