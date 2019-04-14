# -*- coding: utf-8 -*-

#Program written by N. Flesher

"""Program for study of the scriptures"""

# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QLineEdit, QTextEdit, QSplitter, QFrame, QHBoxLayout, QStyleFactory
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import re
import codecs
import json
import ctypes
import time


# ---------------------------------------------------------------------
# OPENING OF FILES & GENERATING OF DICTIONARIES AND LISTS
# ---------------------------------------------------------------------

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
    enjoy = fileenjoy.read()#NEED TO SWAP THIS OUT WITH JSON FILE

# NumbersInScripture Bullinger
with open('./ref_files/number_in_scripture_bullinger.txt', 'r', encoding='ISO-8859-1') as filenumberscript:
    numberscript = filenumberscript.read()#NEED TO SWAP THIS OUT WITH JSON FILE

# WitnessOfTheStars Bullinger
with open('./ref_files/thewitnessofthestars.txt', 'r', encoding='ISO-8859-1') as witnessstars:
    stars = witnessstars.read()#NEED TO SWAP THIS OUT WITH JSON FILE

# TWI scripture index
with open('./ref_files/modified_for_python_SCRIPTURE_INDEX.txt', 'r', encoding='ISO-8859-1') as filetwi:
    twi = filetwi.read()#NEED TO SWAP THIS OUT WITH JSON FILE

# TWI scripture index abbreviations
with open('./ref_files/modified_for_python_SCRIPTURE_INDEX_abbreviations.txt', 'r', encoding='ISO-8859-1') as filetwiabb:
    twiabb = filetwiabb.read()#NEED TO SWAP THIS OUT WITH JSON FILE

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

def sequenceOfFunctions(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func


# ---------------------------------------------------------------------
# SIMR Class
# ---------------------------------------------------------------------

class SIMR(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.program()

        #Text for Pop Ups
        self.about = """\n\n
        About this program:
        --------------------------\n
        This program is called SIMR, which is an abbreviation
        for "Scripture Indices & Ministry Resources."\n
        This program was put together with the python programming
        language, and is a compilation of the works of many, many
        others.  Others who have spent countless hours studying &
        teaching the Word of God.  My thanks to them for making
        researching God's Word so much easier for us!\n
        The goal of this program, is to provide a tool to easily
        compile resources for researching God's Word.  A tool to
        help redeem the time as we diligently study God's Word.
        To 'simmer' is to be at a temperature just below the
        boiling point.  It's to be in a state of the initial
        stages of development...\n
        I thought this fitting, as when we're researching a topic,
        the research we are doing is developing into something more.
        Such as a teaching or a research work.  Not only that, but
        if you desire to boil over with God's Word, to heat to that
        point, you've got to let the Word burn within you.  You
        need to steep in it.  My believing is that this tool will
        help you in your endeavours as you stand for God in this
        day, time, and hour.\n
        Love in Christ,
        N. A. Flesher - 06/03/2018\n"""

        self.credits = """\n\n
        Credits, URL Links, & Resources Used:
        ------------------------------------------------\n
        Strong's Numbers & Definitions - viz.bible\n
        The Holy Bible, Berean Study Bible, BSB
              Copyright ©2016 by Bible Hub
              Used by Permission. All Rights Reserved Worldwide.
              http://berean.bible - Berean Bible Homepage\n
        Data for maps and coordinate locations
        are from OpenBible.info licensed under a
        Creative Commons Attribution license.\n
        Toolbar icons are used under the
        Free License (Creative Common 3.0 Attribution)
        The icons were designed by:
        Double-J Design WEB: http://www.doublejdesign.co.uk
        Email: info@doublejdesign.co.uk\n
        The King James Version, Septuagint, and Strong's
        Concordance, as well Ethelbert W. Bullinger's
        books utilized in this program: The Witness of the Stars,
        Number in Scripture, and How to Enjoy the Bible,
        are all in the public domain.\n
        Thanks to various Christian believers from different
        walks of life, for their typing of the various works,
        for their help in gathering resources, and their advice.\n
        And thanks to YOU, for studying and speaking God's Word!
        YOU ARE GOD'S BEST!!!
        \n\n"""
        
    def program(self):

        self.textEditor = QTextEdit(self)
        self.setCentralWidget(self.textEditor)
        
        #how to append text to text edit area
        #self.textEditor.append('type text here')

        # SEE THIS FIRST - http://zetcode.com/gui/pyqt5/widgets2/
        # SEE - https://www.tutorialspoint.com/pyqt/pyqt_qsplitter_widget.htm
        # SEE - https://www.binpress.com/building-text-editor-pyqt-1/

        # File Menu Options
        newProject = QAction(QIcon('./toolbar_icons/iconfinder_document_basic_blue_69485.png'), '&New Project', self)
        newProject.setStatusTip('Start a new project')
        newProject.setShortcut('Ctrl+N')
        #newProject.triggered.connect(self.)
        
        openProject = QAction(QIcon('./toolbar_icons/iconfinder_folder_basic_blue_69500.png'), '&Open Project', self)
        openProject.setStatusTip('Open an existing project')
        openProject.setShortcut('Ctrl+O')
        #openProject.triggered.connect(self.)

        saveProject = QAction(QIcon('./toolbar_icons/iconfinder_floppy-disk_basic_yellow_70075.png'), '&Save Project', self)        
        saveProject.setStatusTip('Save your current project')
        saveProject.setShortcut('Ctrl+S')
        #saveProject.triggered.connect(self.)

        closeApp = QAction(QIcon('./toolbar_icons/iconfinder_archive_basic_blue_69430.png'), '&Exit', self)        
        closeApp.setStatusTip('Close and exit SIMR')
        closeApp.triggered.connect(qApp.quit)

        # Edit Menu Options
        copyAction = QAction(QIcon('./toolbar_icons/iconfinder_documents_basic_blue_69488'), '&Copy', self)
        copyAction.setStatusTip('Undo your last action')
        copyAction.setShortcut('Ctrl+X')
        copyAction.triggered.connect(self.textEditor.copy)
        
        cutAction = QAction(QIcon('./toolbar_icons/iconfinder_scissors_basic_blue_69570'), '&Cut', self)
        cutAction.setStatusTip('Undo your last action')
        cutAction.setShortcut('Ctrl+C')
        cutAction.triggered.connect(self.textEditor.cut)

        pasteAction = QAction(QIcon('./toolbar_icons/iconfinder_clipboard_basic_green_69665'), '&Paste', self)
        pasteAction.setStatusTip('Undo your last action')
        pasteAction.setShortcut('Ctrl+C')
        pasteAction.triggered.connect(self.textEditor.paste)
        
        undoAction = QAction(QIcon('./toolbar_icons/iconfinder_arrow-left_basic_red_69816.png'), '&Undo', self)
        undoAction.setStatusTip('Undo your last action')
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.textEditor.undo)

        redoAction = QAction(QIcon('./toolbar_icons/iconfinder_arrow-right_basic_yellow_70009.png'), '&Redo', self)
        redoAction.setStatusTip('Redo your last action')
        redoAction.setShortcut('Ctrl+Y')
        redoAction.triggered.connect(self.textEditor.redo)

        selectAll = QAction('&Select All Text', self)
        selectAll.setStatusTip('Select all text in the window')
        selectAll.setShortcut('Ctrl+A')
        selectAll.triggered.connect(self.getAllText)

        clearAll = QAction('&Clear All Text', self)
        clearAll.setStatusTip('Clear all text from the window - CANNOT UNDO')
        clearAll.setShortcut('Ctrl+K')
        clearAll.triggered.connect(self.clearTxt)
        
        # https://www.binpress.com/building-text-editor-pyqt-1/

        appSettings = QAction(QIcon('./toolbar_icons/iconfinder_gears_basic_green_69695.png'), '&Settings', self)
        appSettings.setStatusTip('View and adjust your settings')
        #appSettings.triggered.connect(self.)

        # Search Menu Options
        searchAll = QAction(QIcon('./toolbar_icons/iconfinder_search_basic_blue_69571.png'), '&Search All', self)
        searchAll.setStatusTip('Search through all resources')
        searchAll.triggered.connect(self.getSearchBox)

        # Read Menu Options
        readKJV = QAction(QIcon('./toolbar_icons/iconfinder_book-open-bookmark_basic_blue_69442'), '&King James Version', self)
        readKJV.setStatusTip('Read from the King James Version')
        #readKJV.triggered.connect(self.)

        readKJVwStrongs = QAction(QIcon('./toolbar_icons/iconfinder_book-bookmark_basic_blue_69441'), "&KJV w/ Strong's", self)
        readKJVwStrongs.setStatusTip("Read from the KJV with Strong's numbers")
        #readKJVwStrongs.triggered.connect(self.)

        readSept = QAction(QIcon('./toolbar_icons/iconfinder_book-open-bookmark_basic_yellow_70018'), '&Septuagint', self)
        readSept.setStatusTip('Read from the Septuagint')
        #readSept.triggered.connect(self.)

        readBerean = QAction(QIcon('./toolbar_icons/iconfinder_book-open-bookmark_basic_green_69634'), '&Berean', self)
        readBerean.setStatusTip('Read from the Berean Bible')
        #readBerean.triggered.connect(self.)

        # Books Menu Options
        numberInScripture = QAction('&Number In Scripture', self)
        numberInScripture.setStatusTip('Read from "Number in Scripture" by E. W. Bullinger')
        #numberInScripture.triggered.connect(self.)

        howToEnjoyTheBible = QAction('&How To Enjoy The Bible', self)
        howToEnjoyTheBible.setStatusTip('Read from "How to Enjoy the Bible" by E. W. Bullinger')
        #howToEnjoyTheBible.triggered.connect(self.)

        witnessOfTheStars = QAction('&Witness Of The Stars', self)
        witnessOfTheStars.setStatusTip('Read from "Witness of the Stars" by E. W. Bullinger')
        #witnessOfTheStars.triggered.connect(self.)

        # TWI Menu Options
        scriptureIndex = QAction('&Scripture Index', self)
        scriptureIndex.setStatusTip('Get scripture index for The Way International resources')
        #scriptureIndex.triggered.connect(self.)

        # Scripture Bank Menu Options
        visitScriptureBank = QAction(QIcon('./toolbar_icons/iconfinder_bank_basic_red_69821.png'), '&Visit Scripture Bank', self)
        visitScriptureBank.setStatusTip('Visit your Scripture Bank')
        #visitScriptureBank.triggered.connect(self.)

        depositVerse = QAction('&Deposit Verse', self)
        depositVerse.setStatusTip('Deposit a verse into your Scripture Bank')
        #depositVerse.triggered.connect(self.)

        checkBalance = QAction('&Check Balance', self)
        checkBalance.setStatusTip('Check you Scripture Bank account balance')
        #checkBalance.triggered.connect(self.)

        withdrawVerse = QAction('&Withdraw Verse', self)
        withdrawVerse.setStatusTip('Withdraw a verse from your Scripture Bank')
        #withdrawVerse.triggered.connect(self.)

        # Mapping Menu Options
        drawMap = QAction(QIcon('./toolbar_icons/iconfinder_compass_basic_blue_69477.png'), 'Draw Map', self)
        drawMap.setStatusTip('Draw Bible map')
        #drawMap.triggered.connect(self.)

        # Help Menu Options
        aboutApp = QAction(QIcon('./toolbar_icons/iconfinder_information_basic_green_69706.png'), 'About', self)
        aboutApp.setStatusTip('See information about this application')
        aboutApp.triggered.connect(lambda: self.messBox(self.about, 'About SIMR'))

        appDocumentation = QAction(QIcon('./toolbar_icons/iconfinder_question_basic_green_69755.png'), 'Documentation', self)
        appDocumentation.setStatusTip('See documentation about using this application')
        #appDocumentation.triggered.connect(self.)

        creditsThanks = QAction('Credits / Thanks', self)
        creditsThanks.setStatusTip('See credits and special thanks')
        creditsThanks.triggered.connect(lambda: self.messBox(self.credits, 'SIMR Credits'))

        statusbar = self.statusBar()

        menubar = self.menuBar()

        # File Menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newProject)
        fileMenu.addAction(openProject)
        fileMenu.addAction(saveProject)
        fileMenu.addAction(closeApp)
        
        # Edit Menu
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(copyAction)
        editMenu.addAction(cutAction)
        editMenu.addAction(pasteAction)
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)
        editMenu.addAction(appSettings)
        editMenu.addAction(selectAll)
        editMenu.addAction(clearAll)

        # Search Menu
        searchMenu = menubar.addMenu('&Search')
        searchMenu.addAction(searchAll)

        # Read Menu
        readMenu = menubar.addMenu('&Read')
        readMenu.addAction(readKJV)
        readMenu.addAction(readKJVwStrongs)
        readMenu.addAction(readSept)
        readMenu.addAction(readBerean)

        # Books Menu
        booksMenu = menubar.addMenu('&Books')
        booksMenu.addAction(numberInScripture)
        booksMenu.addAction(howToEnjoyTheBible)
        booksMenu.addAction(witnessOfTheStars)

        # TWI Menu
        twiMenu = menubar.addMenu('&TWI')
        twiMenu.addAction(scriptureIndex)

        # Scripture Bank
        scriptureBankMenu = menubar.addMenu('&Scripture Bank')
        scriptureBankMenu.addAction(visitScriptureBank)
        scriptureBankMenu.addAction(depositVerse)
        scriptureBankMenu.addAction(checkBalance)
        scriptureBankMenu.addAction(withdrawVerse)

        # Mapping Menu
        mappingMenu = menubar.addMenu('&Mapping')
        mappingMenu.addAction(drawMap)

        # Help Menu
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(appDocumentation)
        helpMenu.addAction(creditsThanks)
        helpMenu.addAction(aboutApp)
                
        # Toolbars
        # Main Toolbar
        self.mainToolbar = self.addToolBar('Main Toolbar')
        self.mainToolbar.addAction(newProject)
        self.mainToolbar.addAction(openProject)
        self.mainToolbar.addAction(saveProject)
        self.mainToolbar.addAction(closeApp)
        self.mainToolbar.addAction(copyAction)
        self.mainToolbar.addAction(cutAction)
        self.mainToolbar.addAction(pasteAction)
        self.mainToolbar.addAction(undoAction)
        self.mainToolbar.addAction(redoAction)
        self.mainToolbar.addAction(appSettings)
        self.mainToolbar.addAction(visitScriptureBank)
        self.mainToolbar.addAction(drawMap)
        self.mainToolbar.addAction(appDocumentation)
        self.mainToolbar.addAction(aboutApp)

        # Reading Toolbar
        self.readingToolbar = self.addToolBar('Reading Toolbar')
        self.readingToolbar.addAction(readKJV)
        self.readingToolbar.addAction(readKJVwStrongs)
        self.readingToolbar.addAction(readSept)
        self.readingToolbar.addAction(readBerean)

        # Search Toolbar
        self.searchToolbar = self.addToolBar('Search Toolbar')
        self.searchToolbar.addAction(searchAll)
        self.searchBox = QLineEdit(self.searchToolbar)
        self.searchBox.move(50, 7)
        self.searchBox.resize(150, 25)

        #https://stackoverflow.com/questions/42288320/python-how-to-get-qlineedit-text?rq=1

        # SEE - http://zetcode.com/gui/pyqt5/menustoolbars/

        self.setGeometry(840, 840, 840, 400)
        self.setWindowTitle('SIMR - Scripture Indices and Ministry Resources')    
        self.show()


# /////////////////////////////////////////////////////////////////////
# METHODS OF THE SIMRGUI CLASS
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def textUpdate(self, text):
        self.textEditor.append(text)

    # WRITE A FUNCTION TO SEARCH FOR WORD OR PHRASE TYPED OR SELECTED (RIGHT CLICK MENU)
    # AND RETURN LIST OF VERSES CONTAINING THE SEARCH STRING
    def find_txt(self,text):
        returnedVerses = [i for i in scriptures_lst if text.upper() in i[1].upper()] # THIS IS RETURNING A LIST OF LISTS OF ALL MATCHES (NESTED LIST)
        return returnedVerses
        #CURRENTLY ONLY SETUP TO SEARCH THE KJV

    # Search KJV verse
    def kjv_search(self, verse):#CAN SEARCH FOR A LIST OF VERSES TYPED LIKE JOHN 1:1, aCTS 2:4, james 1:1
        returnedVerses = []
        verses = verse.split(',')
        for v in verses:
            v = v.strip()
            found = next(i for i in scriptures_lst if v in i)
            returnedVerses.append(' - '.join(found))
        return returnedVerses

    # Search KJV w/ Strong's verse
    #Old Testament
    def kjvstrnumOT_search(self, searchOT_ks):
        found_snOT = next(i for i in OT_sn if searchOT_ks in i)
        return found_snOT
    #New Testament
    def kjvstrnumNT_search(self, searchNT_ks):
        found_snNT = next(i for i in NT_sn if searchNT_ks in i)
        return found_snNT

    # Search for Berean verses
    def berean_search(self, berean_inp):
        if berean_inp in berean:
            bi = berean.index(berean_inp)  # This is based on verse seached for.
            # Sets bi to the index of verse searched for
            return bi

    # Search through TWI scripture index
    def twi_scripture_index(self, twi_inp):
        found2 = next(i for i in twi_index if twi_inp in i)
        return found2

    # Search through septuagint
    def septuagint_search(self, sept_inp):
        found3 = next(i for i in septuagint_lst3 if sept_inp in i)
        return found3

    # Search for Strong's defintion
    def strongs_search(self, strongsNumber):
        if strongsNumber in strongscsvlst:
            sc = strongscsvlst.index(strongsNumber)  # This is based on verse seached for.
            # Sets sc to the strongs number searched for
            return sc

    # OT Hebrew Strong's Definitions Search
    def strnumOT(self, OTsearch):
        # OT Strongs Search
        # This finds all <strongs numbers> on all lines printing result without <>
        OTstring = ''.join(OTsearch)
        sn_listOT = re.findall('\<(\d+)\>', OTstring)
        # print(sn_listOT)
        strongsNumberHebrew = []
        for items in sn_listOT:
            hebrew = 'H' + items
            strongsNumberHebrew.append(hebrew)
        # print(hebrew)
        return strongsNumberHebrew

    def get_strongsHebrewDefs(self, strongsNumberHebrew):#THIS DEFINITION PULLS ALL THE HEBREW DEFINITIONS FOR A VERSE
        scH_lst = []
        for item in strongsNumberHebrew:
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
    def strnumNT(self, NTsearch):
        # NT Strongs Search
        # This finds all <strongs numbers> on all lines printing result without <>
        NTstring = ''.join(NTsearch)
        sn_listNT = re.findall('\<(\d+)\>', NTstring)
        # print(sn_listNT)
        strongsNumberGreek = []
        for items in sn_listNT:
            greek = 'G' + items
            strongsNumberGreek.append(greek)
        # print(greek)
        return strongsNumberGreek

    def get_strongsGreekDefs(self, strongsNumberGreek):#THIS DEFINITION PULLS ALL THE GREEK DEFINITIONS FOR A VERSE
        scG_lst = []
        for item in strongsNumberGreek:
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

    def messBox(self, message, title):
        alert = QMessageBox()
        alert.setText(message)
        alert.setWindowTitle(title)
        alert.exec_()

    def searchAll(self, searchText):
                
        #GET KJV
        kjv = self.kjv_search(searchText)
        kjvLabel = "KJV:\n" + '\n\n'.join(kjv)
        
        #GET KJV W/STRONGS
        try:
            kjvs = self.kjvstrnumOT_search(searchText)
        except:
            kjvs = self.kjvstrnumNT_search(searchText)
        kjvsLabel = "KJV w/Strong's - " + ' - '.join(kjvs)
        
        
        #GET SEPTUAGINT
        try:
            sept = self.septuagint_search(searchText)    
            septLabel = "Septuagint - " + ' - '.join(sept)
        except:
            sept = "No verse found in Septuagint for your search..."
            septLabel = "Septuagint - " + sept
        #ISSUES WITH SEPTUAGINT TRY GENESIS 1:1 ALSO SOME JEREMIAH VERSES FOR EXAMPLE - LOOK INTO JSON FILE -
        # json showing first index as "\ufeffGenesis 1:1" - that's the issue

        #berean = self.
        #bereanLabel = 

        #GET TWI SCRIPTURE INDEX
        try:
            twi = self.twi_scripture_index(searchText)
            twiLabel = "Scripture Index : \n" + ' '.join(twi)
        except:
            twiLabel = "Nothing found in Scripture Index for your search..."


        #GET ALL GREEK AND HEBREW DEFINITIONS HERE...
        try:
            ots = self.kjvstrnumOT_search(searchText)
            ots1 = self.strnumOT(ots)
            ots2 = self.get_strongsHebrewDefs(ots1)
            strongsDefinitions = ''.join(ots2)
        except:
            nts = self.kjvstrnumNT_search(searchText)
            nts1 = self.strnumNT(nts)
            nts2 = self.get_strongsGreekDefs(nts1)
            strongsDefinitions = ''.join(nts2)

        return kjvLabel + '\n\n' + kjvsLabel + '\n\n' + strongsDefinitions + '\n\n' + septLabel + '\n\n' + twiLabel

    def getSearchBox(self):
        retrieved = self.searchBox.text()
        self.searchBox.setText('')
        # Search all function here
        text = self.searchAll(retrieved)
        # Return the text to the text editor portion
        self.textUpdate(text)

    # A METHOD TO CLEAR ALL TEXT
    def clearTxt(self):
        self.textEditor.clear()
        #self.statusBar['text'] = "Ready..."

    # COLLECTS ALL TEXT IN THE TEXT WIDGET TO A VARIABLE - USED TO SAVE FILE
    def getAllText(self):
        contents = self.textEditor.selectAll()
        return contents


# ---------------------------------------------------------------------
# Run App
# ---------------------------------------------------------------------
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    simr = SIMR()
    sys.exit(app.exec_())


# ADD A SCRIPTURE BANK WHERE YOU CAN DEPOSIT AND WITHDRAW SCRIPTURES
# https://stackoverflow.com/questions/12602179/pyqt-dynamically-append-to-qtextedit-from-function

