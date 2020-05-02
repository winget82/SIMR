import os
import sqlite3
import sys
import json

db_filename = './SIMR_Bible_Database.db'
schema_filename = './KJV_schema.sql'
tablename = 'kjv_bible'
json_filename = './KJV_json_d.json'
file_path = ''

os.chdir(file_path)

#Read json file
json_file = open(json_filename)
json_data = json.load(json_file)

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as connection:
    if db_is_new:
        print('Making schema...')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        connection.executescript(schema)

        print('Inserting initial data into table...')

            #for loop to read each object in json and insert into sqlite databse
        for key, value in json_data.items():
            print(key,value)
            kjv_scripture = value
            bkcv = key.split(':')
            bkc = bkcv[0]
            kjv_verse = bkcv[1]

            #need to escape the ' character in the verse text because it causes SQL error
            if "'" in kjv_scripture:
                kjv_scripture = kjv_scripture.replace("'", "''")

            #split bkc into list on spaces and grab last item of list as c
            s = bkc.split(' ')
            kjv_chapter = s[-1]

            if len(s) == 3:
                kjv_book = s[0] + ' ' + s[1]

                connection.executescript(
                """
                insert into """ + tablename + """(bible, book, chapter, verse, scripture)
                values ('King James Version', '""" + kjv_book + """', """ + kjv_chapter + """, """ + kjv_verse + """, '""" + kjv_scripture + """');
                """
                )

            else:
                kjv_book = s[0]

                connection.executescript(
                """
                insert into """ + tablename + """(bible, book, chapter, verse, scripture)
                values ('King James Version', '""" + kjv_book + """', """ + kjv_chapter + """, """ + kjv_verse + """, '""" + kjv_scripture + """');
                """
                )

        print("Database made!")

    else:
        print("Database already exists. Exiting now...")
        

json_file.close()
connection.close()