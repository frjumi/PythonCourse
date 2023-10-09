# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
number_of_pages = 100
number_of_rows = 50
number_of_characters = 25
number_of_bits = 4

book_in_bytes = number_of_pages * number_of_rows * number_of_characters * number_of_bits
book_in_megabytes = round(book_in_bytes / 1024**2, 2)
number_of_books = disk_size // book_in_megabytes

print("Количество книг, помещающихся на дискету:", int(number_of_books))
