# SIMR - Scripture Indices & Ministry Resources - Computer Version
# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
import re
from openpyxl import load_workbook
import codecs
import json

# ---------------------------------------------------------------------
"""This script pulls in a verse of your choosing with several available
public domain KJV references to help with studying or putting together a
teaching."""

print("     _____________________   ____________________")
print("  .-/|                    \ /                   |\-.")
print("  ||||  Matthew 4:4       : \  2 Timothy 2:15   ||||")
print('  ||||  "...it is written : | "Study to shew    ||||')
print("  ||||   man shall not    : | thyself approved  ||||")
print("  ||||   live by bread    : | unto GOD, a       ||||")
print("  ||||   alone, but by    : | workman that      ||||")
print("  ||||   every word that  : | needeth not to be ||||")
print("  ||||   proceedeth out   : | ashamed, rightly  ||||")
print("  ||||   of the mouth of  : | dividing the word ||||")
print('  ||||   GOD"             : | of truth"         ||||')
print("  ||||                    : |                   ||||")
print("  ||||                    : |                   ||||")
print("  ||||___________________ : |___________________||||")
print("  ||/====================\: |====================\||")
print("  `---------------------~~| |~-------------------''")
print("                          | | ")
print("                          i^i ")
print("\n\n\n\nGod bless you!  Are you ready to research God's Word?!\n")

# ---------------------------------------------------------------------
# OPENING OF FILES & GENERATING OF DICTIONARIES AND LISTS

fpath = './json_files/'

# Berean Bibles
Berean_file = 'berean_json.json'
with open(fpath + Berean_file) as bereanfile:
    berean = json.load(bereanfile)
    
# KJV
KJV_file = 'KJV_json.json'
with open(fpath + KJV_file) as filekjv:
    scriptures_lst = json.load(filekjv)

books = 'KJVbooks_json.json'
with open(fpath + books) as filebk:
    alph_books = json.load(filebk)

# KJV WITH STRONGS
folderpath = './json_files/StrongsNumbers/'

OT_file = 'OT_json.json'  # OLD TESTAMENT
with open(folderpath + OT_file) as f_obj_OT:
    OT_sn = json.load(f_obj_OT)

NT_file = 'NT_json.json'  # NEW TESTAMENT
with open(folderpath + NT_file) as f_obj_NT:
    NT_sn = json.load(f_obj_NT)

# HowToEnjoyReadingTheBible Bullinger
with open('./ref_files/how_to_enjoy_the_bible_bullinger.txt', 'r', encoding='ISO-8859-1') as fileenjoy:
    enjoy = fileenjoy.read()

# NumbersInScripture Bullinger
with open('./ref_files/number_in_scripture_bullinger.txt', 'r', encoding='ISO-8859-1') as filenumberscript:
    numberscript = filenumberscript.read()

# WitnessOfTheStars Bullinger
with open('./ref_files/thewitnessofthestars.txt', 'r', encoding='ISO-8859-1') as witnessstars:
    stars = witnessstars.read()

# TWI scripture index
with open('./ref_files/modified_for_python_SCRIPTURE_INDEX.txt', 'r', encoding='ISO-8859-1') as filetwi:
    twi = filetwi.read()

# TWI scripture index abbreviations
with open('./ref_files/modified_for_python_SCRIPTURE_INDEX_abbreviations.txt', 'r', encoding='ISO-8859-1') as filetwiabb:
    twiabb = filetwiabb.read()

# Strongs Concordance Dictionary
scd = "strongsconc_json.json"
with open(fpath + scd) as concfile:
    strongscsvlst = json.load(concfile)

# TWI Scripture index split list by verses [verse reference, books & pages & etc.]:
twi_index = [verse.split('\t') for verse
             in twi.split('$') if verse.split('\t')]

# Septuagint
sept = 'septuagint_json.json'
with open(fpath + sept) as sept_file2:
    septuagint_lst3 = json.load(sept_file2)

# ---------------------------------------------------------------------
# FUNCTIONS

# Search KJV verse function
def kjv_search():
    #found = next(i for i in scriptures_lst if kjv_inp in i)
    found = next(i for i in scriptures_lst if verse in i)
    return found

# Search KJV w/ Strong's verse functions
def kjvstrnumOT_search():
    found_snOT = next(i for i in OT_sn if searchOT_ks in i)
    return found_snOT

def kjvstrnumNT_search():
    found_snNT = next(i for i in NT_sn if searchNT_ks in i)
    return found_snNT

# Search for Berean verses function
def berean_search():
    if berean_inp in berean:
        bi = berean.index(berean_inp)  # This is based on verse seached for.
        # Sets bi to the index of verse searched for
        return bi

# Search through TWI scripture index function
def twi_scripture_index():
    found2 = next(i for i in twi_index if twi_inp in i)
    return found2

# Search through septuagint function
def septuagint_search():
    found3 = next(i for i in septuagint_lst3 if sept_inp in i)
    return found3

# Search for Strong's defintion function
def strongs_search():
    inp = input("Enter Strong's Number proceeded by CAPITAL G or H: ")
    if inp in strongscsvlst:
        sc = strongscsvlst.index(inp)  # This is based on verse seached for.
        # Sets sc to the strongs number searched for
        return sc

# OT Hebrew Strong's Definitions Search
def strnumOT(OTsearch):
    # OT Strongs Search
    # This finds all <strongs numbers> on all lines printing result without <>
    OTstring = ''.join(OTsearch)
    sn_listOT = re.findall('\<(\d+)\>', OTstring)
    # print(sn_listOT)
    SNH = []
    for items in sn_listOT:
        hebrew = 'H' + items
        SNH.append(hebrew)
    # print(hebrew)
    return SNH

def get_strhebdefs(SNH):
    scH_lst = []
    for item in SNH:
        if item in strongscsvlst:
            sc = strongscsvlst.index(item)  # This is based on verse seached for.
            # Sets sc to the strongs number searched for
            sc_index0 = strongscsvlst[sc]
            sc_index1 = strongscsvlst[sc + 1]
            sc_index2 = strongscsvlst[sc + 2]
            sc_index3 = strongscsvlst[sc + 3]
            sc_index4 = strongscsvlst[sc + 4]
            sc_index5 = strongscsvlst[sc + 5]
            sc_index6 = strongscsvlst[sc + 6]
            scH = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                   + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                   ' ' + sc_index5 + ', ' + sc_index6 + '\n')
            if scH not in scH_lst:
                scH_lst.append(scH)
    return scH_lst

# NT Greek Strong's Definitions Search
def strnumNT(NTsearch):
    # NT Strongs Search
    # This finds all <strongs numbers> on all lines printing result without <>
    NTstring = ''.join(NTsearch)
    sn_listNT = re.findall('\<(\d+)\>', NTstring)
    # print(sn_listNT)
    SNG = []
    for items in sn_listNT:
        greek = 'G' + items
        SNG.append(greek)
    # print(greek)
    return SNG

def get_strgredefs(SNG):
    scG_lst = []
    for item in SNG:
        if item in strongscsvlst:
            sc = strongscsvlst.index(item)  # This is based on verse seached for.
            # Sets sc to the strongs number searched for
            sc_index0 = strongscsvlst[sc]
            sc_index1 = strongscsvlst[sc + 1]
            sc_index2 = strongscsvlst[sc + 2]
            sc_index3 = strongscsvlst[sc + 3]
            sc_index4 = strongscsvlst[sc + 4]
            sc_index5 = strongscsvlst[sc + 5]
            sc_index6 = strongscsvlst[sc + 6]
            scG = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                   + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                   ' ' + sc_index5 + ', ' + sc_index6 + '\n')
            if scG not in scG_lst:
                scG_lst.append(scG)
    return scG_lst

# ---------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -------------------------------------------------------------------
# LOOP VARIABLES
continue_inquiry = True
strongs_conc = True
rsrchbk = True
bbv_loop = True
sept_loop = True
kjv_loop = True
kjv_str_loop = True
twi_loop = True
# -------------------------------------------------------------------
# Initial Options

while continue_inquiry == True:
    # USER INPUT
    print("\n(N)ote, (BE)rean Bibles, (K)jv, (KS) Kjv w/ Strongs, \n\
	(SE)ptuagint, Strong's Exhaustive (C)oncordance, (R)easearch Books, \n\
The Way Int. Scripture (I)ndex, (CR)edits Etc., (A)bout, (E)xit\n")
    request = input('What would you like to do? ')

    # -------------------------------------------------------------------
    # Add personal Notes

    if request.upper() == 'N':
        note = input('What note would you like to add? ')
        verse_research_file = open('verse_research_file.txt', 'a+')
        verse_research_file.write(note + "\n\n")
        verse_research_file.close()

    # -------------------------------------------------------------------
    # Berean Bible Versions

    elif request.upper() == 'BE':

        while bbv_loop == True:
            b = input('Get Berean Bibles? (Y or N) or (B)ooks of Berean: ')
            if b.upper() == 'Y':
                berean_inp = input('What verse? ')
                bi = berean_search()
                bi_index0 = berean[bi]
                bi_index1 = berean[bi + 1]
                bi_index2 = berean[bi + 2]
                bi_index3 = berean[bi + 3]
                bi_index4 = berean[bi + 4]
                print('\n', bi_index0,
                      '\nBGB (Berean Greek Bible) - ', bi_index1,
                      '\n\nBIB (Berean Interlinear Bible) - ', bi_index2,
                      '\n\nBLB (Berean Literal Bible) - ', bi_index3,
                      '\n\nBSB (Berean Study Bible) - ', bi_index4, '\n\n')

                # WRITE / APPEND VERSES FROM SEARCH TO A TEXT FILE
                # open the file in a+ - append plus mode
                # opens the file for appending to the end of the file (no overwrite) plus read mode
                with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                    verse_research_file.write(bi_index0 +
                                              '\nBGB (Berean Greek Bible) - ' + bi_index1 +
                                              '\n\nBIB (Berean Interlinear Bible) - ' + bi_index2 +
                                              '\n\nBLB (Berean Literal Bible) - ' + bi_index3 +
                                              '\n\nBSB (Berean Study Bible) - ' + bi_index4 + '\n\n')
                    bbv_loop = False

            # Show Books of the Berean Bibles
            elif b.upper() == 'B':
                pass  # NEED TO FINISH THIS CODE

            elif b.upper() == 'N':
                bbv_loop = False

        bbv_loop = True

    # -------------------------------------------------------------------
    # KJV version

    elif request.upper() == 'K':

        while kjv_loop == True:
            k = input('Get KJV Bible? (Y or N) or (B)ooks of KJV: ')
            if k.upper() == 'Y':
                kjv_inp = input('What KJV verses would you like to get?  Separate with a comma "," ').split(',')
                for verse in kjv_inp:
                    verse = verse.strip()
                    search = kjv_search()
                    print()
                    print('KJV - ' + ' - '.join(search) + '\n')

                    # WRITE / APPEND VERSES FROM SEARCH TO A TEXT FILE
                    # open the file in a+ - append plus mode
                    # opens the file for appending to the end of the file (no overwrite) plus read mode
                    with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                        verse_research_file.write('KJV - ' + ' - '.join(search) + "\n")
                kjv_loop = False

            # Show Books of the KJV Bible in Alphabetical Order
            elif k.upper() == 'B':
                print('\n'.join(alph_books))
                kjv_loop = False

            elif k.upper() == 'N':
                kjv_loop = False

        kjv_loop = True

    # -------------------------------------------------------------------
    # KJV version W/ STRONGS NUMBERS

    elif request.upper() == 'KS':

        while kjv_str_loop == True:
            k_s = input("Get KJV w/ Strong's? (Y or N) or (B)ooks of KJV: ")
            if k_s.upper() == 'Y':
                k_s_inp = input('(O)ld Testament or (N)ew Testament? ')
                if k_s_inp.upper() == 'O':
                    searchOT_ks = input('What verse would you like to get? ')
                    OTsearch = kjvstrnumOT_search()
                    OTstrongs = strnumOT(OTsearch)
                    print("\nKJV w/ Strong's - " + ' - '.join(OTsearch) + '\n\n')
                    # print(OTstrongs)
                    Hdefinitions = get_strhebdefs(OTstrongs)
                    print(''.join(Hdefinitions))

                    # WRITE / APPEND VERSES FROM SEARCH TO A TEXT FILE
                    # open the file in a+ - append plus mode
                    # opens the file for appending to the end of the file (no overwrite) plus read mode
                    with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                        verse_research_file.write(
                            "\nKJV w/ Strong's - " + ' - '.join(OTsearch) + '\n\n' + ''.join(Hdefinitions))
                        kjv_str_loop = False

                elif k_s_inp.upper() == 'N':
                    searchNT_ks = input('What verse would you like to get? ')
                    NTsearch = kjvstrnumNT_search()
                    NTstrongs = strnumNT(NTsearch)
                    print("\nKJV w/ Strong's - " + ' - '.join(NTsearch) + '\n\n')
                    # print(NTstrongs)
                    Gdefinitions = get_strgredefs(NTstrongs)
                    print(''.join(Gdefinitions))

                    # WRITE / APPEND VERSES FROM SEARCH TO A TEXT FILE
                    # open the file in a+ - append plus mode
                    # opens the file for appending to the end of the file (no overwrite) plus read mode
                    with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                        verse_research_file.write(
                            "\nKJV w/ Strong's - " + ' - '.join(NTsearch) + '\n\n' + ''.join(Gdefinitions))
                        kjv_str_loop = False

            # Show Books of the KJV Bible in Alphabetical Order
            elif k_s.upper() == 'B':
                print('\n'.join(alph_books))
                kjv_str_loop = False
            elif k_s.upper() == 'N':
                kjv_str_loop = False

        kjv_str_loop = True

    # -------------------------------------------------------------------
    # Way International Scripture Index

    elif request.upper() == 'I':

        while twi_loop == True:
            t = input('Get Way Scripture Index? (Y or N) or (A)bbreviations: ')
            if t.upper() == 'Y':
                twi_inp = input('What verse would you like to look up? ')
                search2 = twi_scripture_index()  # WILL NEED TO SET UP A TRY / EXCEPT FOR WHEN NOTHING IS FOUND FOR THE VERSE
                print('\n\n' + ' '.join(search2))

                # WRITE / APPEND VERSES FROM SEARCH TO A TEXT FILE
                # open the file in a+ - append plus mode
                # opens the file for appending to the end of the file (no overwrite) plus read mode
                with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                    verse_research_file.write('\n' + ' '.join(search2) + "\n")
                    twi_loop == False

            # Make option to show abbreviation meanings
            elif t.upper() == 'A':
                print('\n\n' + twiabb + '\n\n')
                twi_loop = False

            elif t.upper() == 'N':
                twi_loop = False

        twi_loop = True

    # -------------------------------------------------------------------
    # Septuagint

    elif request.upper() == 'SE':  # Add if / elif - books/exit

        while sept_loop == True:
            s = input('Get Septuagint Bible? (Y or N) or (B)ooks of Septuagint: ')
            if s.upper() == 'Y':
                sept_inp = input('What verse would you like to find in the Septuagint? ')
                sept_results = septuagint_search()
                print('\n\nSeptuagint - ' + ' - '.join(sept_results) + '\n\n')

                # WRITE / APPEND STRONGS DEFINITION FROM SEARCH TO A TEXT FILE
                # open the file in a+ - append plus mode
                # opens the file for appending to the end of the file (no overwrite) plus read mode
                with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                    verse_research_file.write('\n\nSeptuagint - ' + ' - '.join(sept_results) + '\n\n')
                    sept_loop = False

            # Show Books of the Septuagint Bible
            elif s.upper() == 'B':  # NEED TO FINISH THIS CODE
                pass

            elif s.upper() == 'N':
                sept_loop = False

        sept_loop = True

    # -------------------------------------------------------------------
    # Strong's Exhaustive Concordance

    elif request.upper() == "C":
        while strongs_conc == True:
            print("What would you like to do with Strong's?")
            strongs_inp = input("Get (D)efinition by Strong's Number, (E)xit: ")

            if strongs_inp.upper() == 'D':
                # Search for Strongs Number
                sc = strongs_search()
                sc_index0 = strongscsvlst[sc]
                sc_index1 = strongscsvlst[sc + 1]
                sc_index2 = strongscsvlst[sc + 2]
                sc_index3 = strongscsvlst[sc + 3]
                sc_index4 = strongscsvlst[sc + 4]
                sc_index5 = strongscsvlst[sc + 5]
                sc_index6 = strongscsvlst[sc + 6]
                print('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                      + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                      ' ' + sc_index5 + ', ' + sc_index6 + '\n')

                # WRITE / APPEND STRONGS DEFINITION FROM SEARCH TO A TEXT FILE
                # open the file in a+ - append plus mode
                # opens the file for appending to the end of the file (no overwrite) plus read mode
                with open('verse_research_file.txt', 'a+', encoding='utf-8') as verse_research_file:
                    verse_research_file.write('\n' + sc_index0 + ' - ' + sc_index1
                                              + ' - ' + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                                              ' ' + sc_index5 + ', ' + sc_index6 + '\n')
                strongs_conc = False

            elif strongs_inp.upper() == 'E':
                strongs_conc = False

        strongs_conc = True

    # -------------------------------------------------------------------
    # Research Works / Books

    elif request.upper() == 'R':
        while rsrchbk == True:
            print('Which would you like to open?')
            researchbook = input('(N)umbers in Scripture, (H)ow to Enjoy the Bible, \
(W)itness of the Stars,\n(F)igures of Speech Used in the Bible, (E)xit: ')

            if researchbook.upper() == 'N':
                print(numberscript)

            if researchbook.upper() == 'H':
                print(enjoy)

            if researchbook.upper() == 'W':
                print(stars)

            # if researchbook.upper() == 'F':
            # print(fos)

            if researchbook.upper() == 'E':
                rsrchbk = False

        rsrchbk = True

    # -------------------------------------------------------------------
    # Credits, Etc.

    elif request.upper() == 'CR':
        print("\n\nCredits, URL Links, & Resources Used:")
        print("-------------------------------------")
        print("Strong's Numbers & Definitions - viz.bible\n")
        print('The Holy Bible, Berean Study Bible, BSB\n',
              'Copyright ©2016 by Bible Hub\n'
              ' Used by Permission. All Rights Reserved Worldwide.\n',
              'http://berean.bible - Berean Bible Homepage\n')
        print("The King James Version, Septuagint, and Strong's")
        print("Concordance, as well Ethelbert W. Bullinger's")
        print('books utilized in this program: The Witness of the Stars,')
        print('Number in Scripture, and How to Enjoy the Bible,')
        print('are all in the public domain.\n')
        print('Thanks to various Christian believers from different')
        print('walks of life, for their typing of the various works,')
        print('for their help in gathering resources, and their advice.\n')
        print("And thanks to YOU, for studying and speaking God's Word!")
        print("YOU ARE GOD'S BEST!!!")
        print("\n\n")

    # -------------------------------------------------------------------
    # About

    # About the program, personal statement
    elif request.upper() == 'A':
        print('\n\nAbout this program:')
        print('This program is called SIMR, which is an abbreviation')
        print('for "Scripture Indices & Ministry Resources."')
        print('\nThis program was put together with the python programming')
        print('language, and is a compilation of the works of many, many')
        print('others.  Others who have spent countless hours studying &')
        print('teaching the Word of God.  My thanks to them for making')
        print("researching God's Word so much easier for us!")
        print('\nThe goal of this program, is to provide a tool to easily')
        print("compile resources for researching God's Word.  A tool to")
        print("help redeem the time as we diligently study God's Word.")
        print("\nTo 'simmer' is to be at a temperature just below the")
        print("boiling point.  It's to be in a state of the initial")
        print("stages of development...\n")
        print("I thought this fitting, as when we're researching a topic,")
        print('the research we are doing is developing into something more.')
        print('Such as a teaching or a research work.  Not only that, but')
        print("if you desire to boil over with God's Word, to heat to that")
        print("point, you've got to let the Word burn within you.  You")
        print('need to steep in it.  My believing is that this tool will')
        print('help you in your endeavours as you stand for God in this')
        print('day, time, and hour.\n')
        print("Love in Christ,")
        print('N. A. Flesher - 06/03/2018\n')

    # -------------------------------------------------------------------
    # Exit Main Program Loop

    # exit from program
    elif request.upper() == 'E':
        continue_inquiry = False
