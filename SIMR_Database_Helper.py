import sqlite3

db_file = "./ref_files/SIMR_Bible_Database.db"

def select_kjv_chapter(db_file, book, chapter):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from kjv_bible where book = ? and chapter = ?"""
        cursor.execute(sql_select_query, (book,chapter,))
        records = cursor.fetchall()
        print("Printing book ", book)
        for row in records:
            print("Bible = ", row[1])
            print("Book = ", row[2])
            print("Chapter = ", row[3])
            print("Verse = ", row[4])
            print("Scripture = ", row[5])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")