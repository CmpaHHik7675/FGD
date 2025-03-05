import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT
);
''')
conn.commit()

def g1():

    # Очистка таблицы (Не обязательно) можно удалить 
    cursor.execute("DELETE FROM books;")
    conn.commit()
    #---------
    
    books = [
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
    ("Moby-Dick", "Herman Melville", 1851, "Adventure"),
    ("War and Peace", "Leo Tolstoy", 1869, "Historical Fiction")
    ]
    cursor.executemany("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?);", books)
    conn.commit()

def g2():
    cursor.execute("SELECT id, title, author, year, genre FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("")
        
def g3():
    print("Введите название книги: ")
    fo = input("/..")
    cursor.execute("SELECT * FROM books WHERE title = ?", (fo,)) 
    rs = cursor.fetchall()
    if rs:
        print(rs)
        print("")
    else:
        print("Книга не найдена.")
    print("")
    
def g4():
    print("Назва книги и новий рік")
    print("Назва книги: ")
    y1 = input("/..")
    print("Новий рік видання: ")
    y2 = input("/..")
    print("")
    try:
        k = int(y2)
    except ValueError:
        print("Невірний рік.")
        print("")
    else:
        cursor.execute("UPDATE books SET year = ? WHERE title = ?", (k, y1))
        conn.commit()
        cursor.execute("SELECT * FROM books WHERE title = ?", (y1,))
        l = cursor.fetchone()
        if l:
            print(f"Книга '{y1}' успішно оновлена. Новий рік видання: {l[3]}")
            print("")
            print("Книги сейчас:")
            g2()
        else:
            print("Книга не знайдена.")
            print("")

            
def g5():
    print("Какую книгу удалить? ")
    ad = input("/..")

    cursor.execute("SELECT * FROM books WHERE title = ?", (ad,))
    ddd = cursor.fetchone()
    if ddd:
        cursor.execute("DELETE FROM books WHERE title = ?", (ad,))
        conn.commit()
        print("Книга успешно удалена.")
        print("")
        print("Книги сейчас:")
        g2()
    else:
        print("Книга не найдена.")
        print("")

g1()
g2()
g3()
g4()
g5()

