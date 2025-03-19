import sqlite3
import os

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);
''')
conn.commit()

def g0():
    os.system('cls' if os.name == 'nt' else 'clear')

def g1():
    cursor.execute("SELECT id, task FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def g2():
    print("Яке завдання редагувати?:")
    g1()
    ad = input("/..")
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (ad,))
    ddd = cursor.fetchone()
    if ddd:
        print("Введіть нове завдання:")
        task = input("\..")
        cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (task, ad))
        conn.commit()
        print("Завдання успішно змінено.")
        print("Завдання зараз: ")
        g6()
        g1()
    else:
        print("Завдання не найдена.")
        g6()


def g3():
    print("Яке завдання додати?:")
    task = input("\..")
    cursor.execute('SELECT MAX(id) FROM tasks')
    mid = cursor.fetchone()[0]
    nid = 1 if mid is None else mid + 1
    cursor.execute('INSERT INTO tasks (id, task) VALUES (?, ?)', (nid, task))
    conn.commit()
    print("Завдання успішно додано.")
    g6()
    
    
def g4():
    print("Яке завдання видалити?:")
    g1()
    ad = input("/..")
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (ad,))
    ddd = cursor.fetchone()
    if ddd:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (ad,))
        conn.commit()
        print("Завдання успішно видалено.")
        print("Завдання зараз: ")
        g6()
        g1()
    else:
        print("Завдання не знайдено.")
        g6()

def g5():
    print("Завдання зараз: ")
    g1()
    print("")
    print("Оберіть опцію:")
    print("1. Повернутися в меню")
    print("2. Сортувати завдання")
    choice = input("\..")
    if choice == '1':
        g6()
        return
    elif choice == '2':
        print("Сортувати за:")
        print("1. За зростанням (ID)")
        print("2. За спаданням (ID)")
        print("3. Переставити завдання місцями (ID)")
        choice = input("\..")
        if choice == '1':
            cursor.execute("SELECT id, task FROM tasks ORDER BY id ASC")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif choice == '2':
            cursor.execute("SELECT id, task FROM tasks ORDER BY id DESC")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif choice == '3':
            try:
                print("Переставити завдання місцями:")
                print("Перше завдання:")
                id1 = input("\..")
                print("Друге завдання:")
                id2 = input("\..")
                cursor.execute("SELECT * FROM tasks WHERE id = ?", (id1,))
                ddd1 = cursor.fetchone()
                cursor.execute("SELECT * FROM tasks WHERE id = ?", (id2,))
                ddd2 = cursor.fetchone()
                if ddd1 and ddd2:
                    cursor.execute("UPDATE tasks SET id = -1 WHERE id = ?", (id1,))
                    cursor.execute("UPDATE tasks SET id = ? WHERE id = ?", (id1, id2))
                    cursor.execute("UPDATE tasks SET id = ? WHERE id = -1", (id2,))
                    conn.commit()
                    print("Завдання успішно переміщено.")
                    print("Завдання зараз:")
                    g6()
                    g1()
                else:
                    g6()
                    print("Завдання не знайдено.")
            except:
                print("Помилка. Спробуйте ще раз.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def g6():    
    cursor.execute("SELECT id, task FROM tasks ORDER BY id ASC")
    rows = cursor.fetchall()
    new_id = 1
    for row in rows:
        cursor.execute("UPDATE tasks SET id = ? WHERE id = ?", (new_id, row[0]))
        new_id += 1
    conn.commit()


while True:
    print("Меню:")
    print("1. Додати задачу")
    print("2. Переглянути/Сортировать задачі")
    print("3. Редагувати задачу")
    print("4. Видалити задачу")
    print("5. Вихід")
    print("Виберіть опцію:")
    choice = input("\..")
    print("")
    if choice == '1':
        print("")
        print("----------||||||||--(Додати задачу)")
        g3()
        print("----------////////--")
        I = input("Для продовження натисніть Enter...")
        g0()
    elif choice == '2':
        print("")
        print("----------||||||||--(Переглянути задачі)")
        g5()
        print("----------////////--")
        I = input("Для продовження натисніть Enter...")
        g0()
    elif choice == '3':
        print("")
        print("----------||||||||--(Редагувати задачу)")
        g2()
        print("----------////////--")
        I = input("Для продовження натисніть Enter...")
        g0()
    elif choice == '4':
        print("")
        print("----------||||||||--(Видалити задачу)")
        g4()
        print("----------////////--")
        I = input("Для продовження натисніть Enter...")
        g0()
    elif choice == '5':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
