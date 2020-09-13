import sqlite3

db_file = "./ref_files/SIMR_Bible_Database.db"

def select_kjv_book_chapter(db_file, book, chapter):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from kjv_bible where book = ? and chapter = ?"""
        cursor.execute(sql_select_query, (book,chapter,))
        records = cursor.fetchall()
        scripture_string = ""
        #print("Printing book ", book)
        for row in records:
            scripture_string += '(' + str(row[4]) + ') ' + str(row[5]) + '\n'
            #print("Bible = ", row[1])
            #print("Book = ", row[2])
            #print("Chapter = ", row[3])
            #print("Verse = ", row[4])
            #print("Scripture = ", row[5])
        cursor.close()

        return scripture_string

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_books(db_file):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        books_lst = []

        sql_select_query = """select distinct book from kjv_bible"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            books_lst.append(row[0])
        cursor.close()

        return books_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def get_kjv_chapters(db_file, book):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        chapters_lst = []

        sql_select_query = """select distinct chapter from kjv_bible where book = ?"""
        cursor.execute(sql_select_query, (book,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            chapters_lst.append(row[0])
        cursor.close()

        return chapters_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_verses(db_file, book, chapter):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        verses_lst = []

        sql_select_query = """select distinct verses from kjv_bible where book = ? and chapter = ?"""
        cursor.execute(sql_select_query, (book, chapter,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            verses_lst.append(row[0])
        cursor.close()

        return verses_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_scripture(db_file, book, chapter, verse):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        scripture = ""
        sql_select_query = """select scripture from kjv_bible where book = ? and chapter = ? and verse = ?"""
        cursor.execute(sql_select_query, (book, chapter, verse,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            scripture = row[0]
        cursor.close()

        return scripture

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

#--------------------------------------------------------------------------------------------------------

def select_kjv_strongs_book_chapter(db_file, book, chapter):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from kjv_strongs_bible where book = ? and chapter = ?"""
        cursor.execute(sql_select_query, (book,chapter,))
        records = cursor.fetchall()
        scripture_string = ""
        #print("Printing book ", book)
        for row in records:
            scripture_string += '(' + str(row[4]) + ') ' + str(row[5]) + '\n'
            #print("Bible = ", row[1])
            #print("Book = ", row[2])
            #print("Chapter = ", row[3])
            #print("Verse = ", row[4])
            #print("Scripture = ", row[5])
        cursor.close()

        return scripture_string

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_strongs_books(db_file):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        books_lst = []

        sql_select_query = """select distinct book from kjv_strongs_bible"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            books_lst.append(row[0])
        cursor.close()

        return books_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_strongs_chapters(db_file, book):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        chapters_lst = []

        sql_select_query = """select distinct chapter from kjv_strongs_bible where book = ?"""
        cursor.execute(sql_select_query, (book,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            chapters_lst.append(row[0])
        cursor.close()

        return chapters_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_strongs_verses(db_file, book, chapter):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        verses_lst = []

        sql_select_query = """select distinct verses from kjv_strongs_bible where book = ? and chapter = ?"""
        cursor.execute(sql_select_query, (book, chapter,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            verses_lst.append(row[0])
        cursor.close()

        return verses_lst

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_kjv_strongs_scripture(db_file, book, chapter, verse):
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        scripture = ""
        sql_select_query = """select scripture from kjv_strongs_bible where book = ? and chapter = ? and verse = ?"""
        cursor.execute(sql_select_query, (book, chapter, verse,))
        records = cursor.fetchall()
        
        for row in records:
            #print(row[0])
            scripture = row[0]
        cursor.close()

        return scripture

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")