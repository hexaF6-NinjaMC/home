
scriptures = ["Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", "Pearl of Great Price"]
book_of_mormon_list = []
book_list = []
interest_scriptures = []

with open('C:/Users/becht/Desktop/Python & Coding/books_and_chapters.txt') as text_file:
    for line in text_file:
        clean_line = line.strip()
        separated_line = clean_line.split(':')
        book_list.append(separated_line)

for scripture in scriptures:
    print(scripture)

interest_user_book = input("Which book would like to learn: ")

if interest_user_book.lower() == "old testament":
    for book_quality in book_list:
        if book_quality[2] == "Old Testament":
            
            interest_scriptures.append(book_quality)

            print(f'Scripture: {book_quality[2]}, Book: {book_quality[0]}, Chapters: {book_quality[1]}')

            max_chapter = 0
            max_book = ''

            for old_testament_qual in interest_scriptures:
                chapter = int(old_testament_qual[1])
                if chapter > max_chapter:
                    max_chapter = chapter
                    max_book = old_testament_qual[0]

if interest_user_book.lower() == "new testament":
    for book_quality in book_list:
        if book_quality[2] == "New Testament":
            
            interest_scriptures.append(book_quality)

            print(f'Scripture: {book_quality[2]}, Book: {book_quality[0]}, Chapters: {book_quality[1]}')

            max_chapter = 0
            max_book = ''

            for new_testament_qual in interest_scriptures:
                chapter = int(new_testament_qual[1])
                if chapter > max_chapter:
                    max_chapter = chapter
                    max_book = new_testament_qual[0]

if interest_user_book.lower() == "book of mormon":
    for book_quality in book_list:
        if book_quality[2] == "Book of Mormon":
            
            interest_scriptures.append(book_quality)

            print(f'Scripture: {book_quality[2]}, Book: {book_quality[0]}, Chapters: {book_quality[1]}')

            max_chapter = 0
            max_book = ''

            for book_of_mormon_qual in interest_scriptures:
                chapter = int(book_of_mormon_qual[1])
                if chapter > max_chapter:
                    max_chapter = chapter
                    max_book = book_of_mormon_qual[0]

if interest_user_book.lower() == "doctrine and covenants":
    for book_quality in book_list:
        if book_quality[2] == "Doctrine and Covenants":
            
            interest_scriptures.append(book_quality)

            print(f'Scripture: {book_quality[2]}, Book: {book_quality[0]}, Chapters: {book_quality[1]}')

            max_chapter = 0
            max_book = ''

            for doctrine_and_covenants_qual in interest_scriptures:
                chapter = int(doctrine_and_covenants_qual[1])
                if chapter > max_chapter:
                    max_chapter = chapter
                    max_book = doctrine_and_covenants_qual[0]

if interest_user_book.lower() == "pearl of great price":
    for book_quality in book_list:
        if book_quality[2] == "Pearl of Great Price":
            
            interest_scriptures.append(book_quality)

            print(f'Scripture: {book_quality[2]}, Book: {book_quality[0]}, Chapters: {book_quality[1]}')

            max_chapter = 0
            max_book = ''

            for pearl_of_great_price_qual in interest_scriptures:
                chapter = int(pearl_of_great_price_qual[1])
                if chapter > max_chapter:
                    max_chapter = chapter
                    max_book = pearl_of_great_price_qual[0]

book = ''

for piece in interest_scriptures:
    book = piece[2]

print(f"Largest numbers of chapters in the {book} is {max_chapter} in the book of {max_book}.")
