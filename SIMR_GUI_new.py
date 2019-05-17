# -*- coding: utf-8 -*-

#Program written by N. Flesher

"""Program for study of the scriptures"""

# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QLineEdit, QTextEdit, QSplitter, QFrame, QHBoxLayout, QSizePolicy, QVBoxLayout, QStyleFactory, QFileDialog, QInputDialog, QDialog, QRadioButton, QComboBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot
import re
import codecs
import json
import ctypes
import time
import _pickle as cpickle
from collections import OrderedDict


# ---------------------------------------------------------------------
# OPENING OF FILES & GENERATING OF DICTIONARIES AND LISTS
# ---------------------------------------------------------------------

# Set filepath directory for json files
fpath = './json_files/'

# Berean Bibles
Berean_file = 'berean_json.json'
with open(fpath + Berean_file) as bereanfile:
    berean = json.load(bereanfile)
    
# KJV
KJV_file = 'KJV_json.json'
with open(fpath + KJV_file) as filekjv:
    scriptures_lst = json.load(filekjv)

# Generate Notes list (currently KJV only)
notes_lst = []
for i in scriptures_lst:
    notes_lst.append(next(j for j in i))# This generates a list of only book chapter:verse
    # Turn all of these list items into dictionary keys with empty lists for values
notes_dictionary_kjv = dict((keys, []) for keys in notes_lst)
    # when loading in notes, these list values will need to be populated from previously saved data if loaded
    # will need to do this same type of thing for each version of the bible, unless you come up with a better way of doing it

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
# Classes
# ---------------------------------------------------------------------

class NotesWindow(QMainWindow):

    def __init__(self, parent=None):
        super(NotesWindow, self).__init__(parent)
        self.userInterfaceNotes()

    def userInterfaceNotes(self):

        statusbar = self.statusBar()

        self.setGeometry(500, 500, 840, 400)
        #self.spacer = QFrame(self) # could try using a QFrame as spacer
        # look into sizepolicy

        self.notesEditor = QTextEdit(self)
        #self.setCentralWidget(self.notesEditor)
        #self.notesEditor.move(0,70)# - this moves notesEditor down if setCentralWidget not used
        self.notesEditor.setGeometry(0, 70, 840, 330)
        #self.notesEditor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # need to determine how to set the horizontal to expand with the window
        # MAY PUT THE SIZING ISSUES ABOVE OFF UNTIL LATER AND FOCUS ON GETTING THE NOTES TO PULL IN AND SAVE OUT ETC.********************
        
        #self.notesEditor.setTextColor() # set text to blue
        
        viewNotes = QAction('&View Notes', self)
        viewNotes.setStatusTip('Look at notes')
        viewNotes.triggered.connect(self.pullNotes)

        saveNotes = QAction('&Save Notes', self)
        saveNotes.setStatusTip('Save notes')
        saveNotes.triggered.connect(self.saveNotes)

        notesMenuBar = self.menuBar()
        notesMenu = notesMenuBar.addMenu('&My Notes')
        notesMenu.addAction(viewNotes)
        notesMenu.addAction(saveNotes)

        # SEE notes_dictionary_kjv

        # Add a notes section using dictionaries, with keys being the book chapter and verse and values being a list of strings
        # for example:
        # notes_dictionary_kjv['Acts 1:1'].append('This is a great verse')
        # >>>notes_dictionary_kjv['Acts 1:1'][0]
        # 'This is a great verse'

        # ***Look into making notes window dockable***

        # MAY NEED TO DO A REGEX OR SOMETHING ABOUT WHEN THE STRING FOR A PERSON'S NOTE CONTAINS A ' OR A " TO ESCAPE IT SO IT WILL PRINT CORRECTLY AND NOT ERROR
        # THIS NOTES DICTIONARY WILL NEED SAVED AS A FILE 
        # ALSO MAY WANT TO HAVE A DROP DOWN, DRAG AND DROP, OR VARIABLE OR SOMETHING TO KNOW WHAT VERSE TO ADD AS THE KEY, CLEANLY

        # https://pythonprogramming.net/drop-down-button-window-styles-pyqt-tutorial/

        self.comboBoxBooks = QComboBox(self)
        self.comboBoxBooks.setToolTip('Choose Book')
        self.comboBoxChapters = QComboBox(self)
        self.comboBoxChapters.setToolTip('Choose Chapter')
        #self.comboBoxChapters.setDuplicatesEnabled(False) #this is NOT preventing duplicates
        self.comboBoxVerses = QComboBox(self)
        self.comboBoxVerses.setToolTip('Choose Verse')

        # Split into nested lists [['1 Samuel','1','12'], ['2 Corinthians','2','1']], etc.
        self.kjvBreakLst = []

        for i in notes_lst:
            temp = re.split(r'\s(\d+):', i)
            self.kjvBreakLst.append(temp)
            
            # THIS WILL HAVE TO BE DYNAMIC PER BOOK SELECTED, THEN PER CHAPTER SELECTED
            # OTHERWISE IT WILL NOT POPULATE CORRECTLY
        
        kjvBooks = []

        for verseReference in self.kjvBreakLst:
            kjvBooks.append(verseReference[0])
        
        kjvBooksFinal = list(OrderedDict.fromkeys(kjvBooks))

        for book in kjvBooksFinal:
            self.comboBoxBooks.addItem(book)

        self.comboBoxBooks.activated.connect(lambda: self.chapters(book))
        self.comboBoxChapters.activated.connect(lambda: self.verses(book))

        # here I need an action when verse is selected, to automatically pull up any notes for that verse - in text editor
        # need to pull value of each combo box into a variable scriptureReference
        self.comboBoxVerses.activated.connect(self.pullNotes)

        self.saveNotesButton = QPushButton('Save Notes', self)
        self.saveNotesButton.setToolTip('Save your notes for selected verse')
        self.saveNotesButton.clicked.connect(self.saveNotes)

        self.deleteNotesButton = QPushButton('Delete Notes', self)
        self.deleteNotesButton.setToolTip('Delete your notes for selected verse')
        self.deleteNotesButton.clicked.connect(self.deleteNotes)

        
        self.comboBoxBooks.move(20, 30)
        self.comboBoxChapters.move(120, 30)
        self.comboBoxVerses.move(220, 30)
        self.saveNotesButton.move(420, 30)
        self.deleteNotesButton.move(520, 30)


    def chapters(self, book):
        self.notesEditor.clear()
        self.comboBoxChapters.clear()
        self.comboBoxVerses.clear()
        temp = [] #temporary list to prevent duplicates by adding the number to the list after added to combobox
        currentBook = str(self.comboBoxBooks.currentText())
        for verseReference in self.kjvBreakLst:
            if currentBook in verseReference[0]:                
                if verseReference[1] not in temp:
                    self.comboBoxChapters.addItem(verseReference[1])
                    temp.append(verseReference[1])


    def verses(self, book):
        self.notesEditor.clear()
        self.comboBoxVerses.clear()
        temp = [] #temporary list to prevent duplicates by adding the number to the list after added to combobox
        currentBook = str(self.comboBoxBooks.currentText())
        currentChapter = str(self.comboBoxChapters.currentText())
        for verseReference in self.kjvBreakLst:
            if currentBook in verseReference[0]: 
                if currentChapter in verseReference[1]:                
                    if verseReference[2] not in temp:
                        self.comboBoxVerses.addItem(verseReference[2])
                        temp.append(verseReference[2])


    def getScriptureReference(self):

        book = self.comboBoxBooks.currentText()
        chapter = self.comboBoxChapters.currentText()
        verse = self.comboBoxVerses.currentText()

        # combine into scriptureReference
        scriptureReference = book + ' ' + chapter + ':' + verse

        return scriptureReference


    def pullNotes(self):

        scriptureReference = self.getScriptureReference()
        # clear notes from text window
        self.notesEditor.clear()

        # pull notes for selected verse and update text on window
        for note in notes_dictionary_kjv[scriptureReference]:
            self.notesEditor.append(note)


    # have a toolbar button to save current note changes    
    def saveNotes(self):

        scriptureReference = self.getScriptureReference()

        notes = self.notesEditor.toPlainText()
        #replace previous value
        notes_dictionary_kjv[scriptureReference] = [notes]
        # save to pickle file also

        #FOUND AN ERROR - NO JOHN 2:26 IN notes_dictionary_kjv - WILL NEED TO RUN TESTS TO MAKE SURE ALL VERSES ARE ACCOUNTED FOR

    def deleteNotes(self):
        
        self.notesEditor.clear()
        scriptureReference = self.getScriptureReference()

        #replace previous value with empty list
        notes_dictionary_kjv[scriptureReference] = []

    def loadNotes(self):
        # load notes dictionary from pickle file
        with open("notes_kjv.dat", 'rb') as f:
            notes_dictionary_kjv = cpickle.load(f)


class MapWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MapWindow, self).__init__(parent)
        self.userInterfaceMapping()

    def userInterfaceMapping(self):
        """
        Leave triple quoted - generates error on linux if simply commented out
        - until the code is resolved for this aspect of the program
        focus on other areas first
        # import pandas as pd
        # from shapely.geometry import Point
        # import geopandas as gpd
        # from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        # from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
        # import matplotlib.pyplot as plt
        """
        # https://pythonspot.com/pyqt5-matplotlib/

        # https://stackoverflow.com/questions/24675484/different-dataframe-plotting-behaviour-when-using-figurecanvasqtagg

        # https://stackoverflow.com/questions/12459811/how-to-embed-matplotlib-in-pyqt-for-dummies

        statusbar = self.statusBar()

        self.setGeometry(200, 200, 840, 400)

        findLocation = QAction('&Find Location', self)
        findLocation.setStatusTip('Search for a location')
        # findLocation.triggered.connect(self.plot)

        mapMenuBar = self.menuBar()
        mapMenu = mapMenuBar.addMenu('&Search')
        mapMenu.addAction(findLocation)

        self.mappingToolbar = self.addToolBar('Mapping Toolbar')
        self.mappingToolbar.addAction(findLocation)

        # Will need to acknowledge sources of shapefile in credits section - Natural Earth
        #self.world = gpd.read_file(r'./ref_files/NaturalEarth/ne_10m_land/ne_10m_land.shp')
        #self.cities = pd.read_csv(r'./ref_files/OpenBible.Info/places_edited.csv')
        #self.countries = gpd.read_file(r'./ref_files/NaturalEarth/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp')
        #self.oceans = gpd.read_file(r'./ref_files/NaturalEarth/ne_10m_ocean/ne_10m_ocean.shp')    

        # plot world to map
        #base = self.world.plot(color='tan', edgecolor='black')

        # convert csv city points to geometry
        #geometry = [Point(xy) for xy in zip(self.cities['Lon'], self.cities['Lat'])]
        #crs = {'init': 'epsg:4326'}#set crs to wgs84
        #gdf = gpd.GeoDataFrame(self.cities, crs=crs, geometry=geometry)

        # plot cities to map
        #pl = gdf.plot(ax=base, marker='o', color='r', markersize=5)

        # label cities (very slow)
        # for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf.ESV):
        #    pl.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")

        # add wgs84 bounding box
        # wgs84.plot(ax=base, facecolor='none', edgecolor = 'cyan')

        # add countries' borders
        #self.countries.plot(ax=base, facecolor='none', edgecolor = 'black')

        # plot oceans
        #self.oceans.plot(ax=base, color='lightblue')

        # set layers to same crs as cities (coordinate reference system as cities)
        #self.world = self.world.to_crs(gdf.crs)
        # wgs84 = wgs84.to_crs(gdf.crs)
        #self.countries = self.countries.to_crs(gdf.crs)
        #self.oceans = self.oceans.to_crs(gdf.crs)
     

class ScriptureBankWindow(QMainWindow):

    def __init__(self, parent=None):
        super(ScriptureBankWindow, self).__init__(parent)
        self.userInterfaceScriptureBank()

    def userInterfaceScriptureBank(self):

        statusbar = self.statusBar()

        self.setGeometry(300, 300, 840, 400)
        
        depositVerse = QAction('&Deposit Verse', self)
        depositVerse.setStatusTip('Deposit a verse into your Scripture Bank')
        #depositVerse.triggered.connect(self.)

        checkBalance = QAction('&Check Balance', self)
        checkBalance.setStatusTip('Check your Scripture Bank account balance')
        #checkBalance.triggered.connect(self.)

        withdrawVerse = QAction('&Withdraw Verse', self)
        withdrawVerse.setStatusTip('Withdraw a verse from your Scripture Bank')
        #withdrawVerse.triggered.connect(self.)
        
        scriptureBankMenubar = self.menuBar()

        # Bank Menu
        bank = scriptureBankMenubar.addMenu('&Scripture Bank')
        bank.addAction(depositVerse)
        bank.addAction(checkBalance)
        bank.addAction(withdrawVerse)
        
        self.scriptureBankToolbar = self.addToolBar('Scripture Bank Toolbar')
        self.scriptureBankToolbar.addAction(depositVerse)
        self.scriptureBankToolbar.addAction(checkBalance)
        self.scriptureBankToolbar.addAction(withdrawVerse)

        # ADD A SECTION FOR MAKING / READING NOTES - COULD UTILIZE A DICTIONARY, WITH KEY BEING THE VERSE AND VALUE BEING A LIST OF NOTE STRINGS


class ReadingWindow(QMainWindow):

    def __init__(self, parent=None):
        super(ReadingWindow, self).__init__(parent)
        self.userInterfaceReading()

    def userInterfaceReading(self):

        statusbar = self.statusBar()

        self.setGeometry(400, 400, 840, 400)

        # SEE QTextBrowser (supports hypertext which would make easier navigation) for reading text
        # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QTextBrowser.html
        # https://stackoverflow.com/questions/49852012/python-pyqt5-set-text-to-qtextbrowser-with-different-colors
        # https://www.programcreek.com/python/example/108079/PyQt5.QtWidgets.QTextBrowser

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
        witnessOfTheStars.triggered.connect(lambda: self.printOut(stars))

        readingMenubar = self.menuBar()
        
        # Books Menu
        booksMenu = readingMenubar.addMenu('&Books')
        booksMenu.addAction(numberInScripture)
        booksMenu.addAction(howToEnjoyTheBible)
        booksMenu.addAction(witnessOfTheStars)

        # Reading Toolbar
        self.readingToolbar = self.addToolBar('Reading Toolbar')
        self.readingToolbar.addAction(readKJV)
        self.readingToolbar.addAction(readKJVwStrongs)
        self.readingToolbar.addAction(readSept)
        self.readingToolbar.addAction(readBerean)
        self.readingToolbar.addAction(numberInScripture)
        self.readingToolbar.addAction(howToEnjoyTheBible)
        self.readingToolbar.addAction(witnessOfTheStars)

        # ADD A SECTION FOR MAKING / READING NOTES - COULD UTILIZE A DICTIONARY, WITH KEY BEING THE VERSE AND VALUE BEING A LIST OF NOTE STRINGS


class SIMR(QMainWindow):
    
    def __init__(self, parent=None):
        super(SIMR, self).__init__(parent)
        self.userInterface()

        # Text for Pop Ups
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
        
    def userInterface(self):

        self.textEditor = QTextEdit(self)
        self.setCentralWidget(self.textEditor)

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
        saveProject.triggered.connect(self.saveProject)

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
        pasteAction.setShortcut('Ctrl+V')
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
        selectAll.triggered.connect(self.textEditor.selectAll)

        clearAll = QAction('&Clear All Text', self)
        clearAll.setStatusTip('Clear all text from the window - CANNOT UNDO')
        clearAll.setShortcut('Ctrl+K')
        clearAll.triggered.connect(self.clearTxt)
        
        # https://www.binpress.com/building-text-editor-pyqt-1/

        appSettings = QAction(QIcon('./toolbar_icons/iconfinder_gears_basic_green_69695.png'), '&Settings', self)
        appSettings.setStatusTip('View and adjust your settings')
        #appSettings.triggered.connect(self.)

        # Search Menu Options
        searchAll = QAction(QIcon('./toolbar_icons/iconfinder_search_basic_blue_69571.png'), '&Search', self)
        searchAll.setStatusTip('Search resources')
        searchAll.triggered.connect(self.radioSearch)

        findText = QAction(QIcon('./toolbar_icons/iconfinder_search_basic_blue_69571.png'), '&Find', self)
        findText.setStatusTip('Search for text')
        findText.triggered.connect(lambda: self.textUpdate(self.find_txt(self.getTextSearchBox())))

         # Read Menu Options
        launchReadingWindow = QAction(QIcon('./toolbar_icons/iconfinder_weather-sun_basic_yellow_70186.png'), '&Reading Window', self)
        launchReadingWindow.setStatusTip('Launch the reading window')
        self.readingWindow = ReadingWindow(self)
        self.readingWindow.setWindowTitle('Reading Window')
        launchReadingWindow.triggered.connect(self.readingWindow.show)
        
        # TWI Menu Options
        scriptureIndex = QAction('&Scripture Index', self)
        scriptureIndex.setStatusTip('Get scripture index for The Way International resources')
        #scriptureIndex.triggered.connect(self.)

        # Scripture Bank Menu Options
        visitScriptureBank = QAction(QIcon('./toolbar_icons/iconfinder_bank_basic_red_69821.png'), '&Visit Scripture Bank', self)
        visitScriptureBank.setStatusTip('Visit your Scripture Bank')
        self.scriptureBankWindow = ScriptureBankWindow(self)
        self.scriptureBankWindow.setWindowTitle('Scripture Bank Window')
        visitScriptureBank.triggered.connect(self.scriptureBankWindow.show)
        
        # Mapping Menu Options
        drawMap = QAction(QIcon('./toolbar_icons/iconfinder_compass_basic_blue_69477.png'), 'Draw Map', self)
        drawMap.setStatusTip('Draw Bible map')
        self.mapWindow = MapWindow(self)
        self.mapWindow.setWindowTitle('Map Window')
        drawMap.triggered.connect(self.mapWindow.show)
        
        # Notes Menu Options
        notes = QAction(QIcon('./toolbar_icons/iconfinder_quill_basic_blue_69566.png'), 'Notes', self)
        notes.setStatusTip('Edit Notes')
        self.notesWindow = NotesWindow(self)
        self.notesWindow.setWindowTitle('Notes Window')
        notes.triggered.connect(self.notesWindow.show)


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

        # Menu Bar
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
        readMenu.addAction(launchReadingWindow)
      
        # TWI Menu
        twiMenu = menubar.addMenu('&TWI')
        twiMenu.addAction(scriptureIndex)

        # Scripture Bank
        scriptureBankMenu = menubar.addMenu('&Scripture Bank')
        scriptureBankMenu.addAction(visitScriptureBank)

        # Mapping Menu
        mappingMenu = menubar.addMenu('&Mapping')
        mappingMenu.addAction(drawMap)

        # Notes Menu
        notesMenu = menubar.addMenu('&Notes')
        notesMenu.addAction(notes)

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
        self.mainToolbar.addAction(notes)
        self.mainToolbar.addAction(launchReadingWindow)
        self.mainToolbar.addAction(visitScriptureBank)
        self.mainToolbar.addAction(drawMap)
        self.mainToolbar.addAction(appDocumentation)
        self.mainToolbar.addAction(aboutApp)

        # GreekHebrew Toolbar
        self.greekHebrewToolbar = self.addToolBar('Greek Hebrew Toolbar')
        self.radioButtonHebrew = QRadioButton("Hebrew")
        self.radioButtonHebrew.toggled.connect(lambda: radioButtonColorChange(self.radioButtonHebrew))
        self.radioButtonGreek = QRadioButton("Greek")
        self.radioButtonGreek.toggled.connect(lambda: radioButtonColorChange(self.radioButtonGreek))
        self.greekHebrewToolbar.addWidget(self.radioButtonHebrew)
        self.greekHebrewToolbar.addWidget(self.radioButtonGreek)
        self.searchHebrewGreekBox = QLineEdit()
        self.greekHebrewToolbar.addWidget(self.searchHebrewGreekBox)
        
        searchGreekHebrew = QAction(QIcon('./toolbar_icons/iconfinder_search_basic_blue_69571.png'), '&Search Hebrew Greek', self)
        searchGreekHebrew.setStatusTip('Search for Hebrew and Greek definitions')
        searchGreekHebrew.triggered.connect(self.greekHebrewRadioSearch)

        self.greekHebrewToolbar.addAction(searchGreekHebrew)

        # Break between toolbars
        self.addToolBarBreak()

        # Search Toolbar
        self.searchToolbar = self.addToolBar('Search Toolbar')
        
        self.radioButtonSearchAll = QRadioButton("Search All")
        self.radioButtonSearchAll.toggled.connect(lambda: radioButtonColorChange(self.radioButtonSearchAll))
        self.radioButtonKJV = QRadioButton("KJV")
        self.radioButtonKJV.toggled.connect(lambda: radioButtonColorChange(self.radioButtonKJV))
        self.radioButtonKJVwStrongs = QRadioButton("KJV w/ Strong's")
        self.radioButtonKJVwStrongs.toggled.connect(lambda: radioButtonColorChange(self.radioButtonKJVwStrongs))
        self.radioButtonSeptuagint = QRadioButton("Septuagint")
        self.radioButtonSeptuagint.toggled.connect(lambda: radioButtonColorChange(self.radioButtonSeptuagint))
        self.radioButtonBerean = QRadioButton("Berean")
        self.radioButtonBerean.toggled.connect(lambda: radioButtonColorChange(self.radioButtonBerean))
        self.radioButtonScriptureIndex = QRadioButton("Scripture Index")
        self.radioButtonScriptureIndex.toggled.connect(lambda: radioButtonColorChange(self.radioButtonScriptureIndex))
        
        self.searchToolbar.addWidget(self.radioButtonSearchAll)
        self.searchToolbar.addWidget(self.radioButtonKJV)
        self.searchToolbar.addWidget(self.radioButtonKJVwStrongs)
        self.searchToolbar.addWidget(self.radioButtonSeptuagint)
        self.searchToolbar.addWidget(self.radioButtonBerean)
        self.searchToolbar.addWidget(self.radioButtonScriptureIndex)

        self.searchBox = QLineEdit()
        self.searchToolbar.addWidget(self.searchBox)
        self.searchToolbar.addAction(searchAll)
        
        # Break between toolbars
        self.addToolBarBreak()

        # Text Search Toolbar
        self.textSearchToolbar = self.addToolBar('Text Search Toolbar')
        self.textSearchBox = QLineEdit()
        self.textSearchToolbar.addWidget(self.textSearchBox)
        self.textSearchToolbar.addAction(findText)

        # Function to change color of selected radio button and text
        def radioButtonColorChange(radioButtonName):
            if radioButtonName.isChecked():
                radioButtonName.setStyleSheet("color: red")
            else:
                radioButtonName.setStyleSheet("color: black")

        self.setWindowTitle('SIMR - Scripture Indices and Ministry Resources')

        # Open main window defaulted to maximized window
        self.showMaximized()


# /////////////////////////////////////////////////////////////////////
# METHODS OF THE SIMRGUI CLASS
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def textUpdate(self, text):
        self.textEditor.append(text)
    
    # WRITE A FUNCTION TO SEARCH FOR WORD OR PHRASE TYPED OR SELECTED (RIGHT CLICK MENU)
    # AND RETURN LIST OF VERSES CONTAINING THE SEARCH STRING
    def find_txt(self,text):
        returnedVerses = [i for i in scriptures_lst if text.upper() in i[1].upper()] # THIS IS RETURNING A LIST OF LISTS OF ALL MATCHES (NESTED LIST)
        # join lists and nested lists to a string to be returned
        versesFound = list(map(' - '.join, returnedVerses))
        returnedVerses = '\n'.join(versesFound)
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
    # Old Testament
    def kjvstrnumOT_search(self, searchOT_ks):
        found_snOT = next(i for i in OT_sn if searchOT_ks in i)
        return found_snOT
    # New Testament
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
                
        # GET KJV
        kjv = self.kjv_search(searchText)
        kjvLabel = "KJV:\n" + '\n\n'.join(kjv)
        
        # GET KJV W/STRONGS
        try:
            kjvs = self.kjvstrnumOT_search(searchText)
        except:
            kjvs = self.kjvstrnumNT_search(searchText)
        kjvsLabel = "KJV w/Strong's - " + ' - '.join(kjvs)
        
        # GET SEPTUAGINT
        try:
            sept = self.septuagint_search(searchText)    
            septLabel = "Septuagint - " + ' - '.join(sept)
        except:
            sept = "No verse found in Septuagint for your search..."
            septLabel = "Septuagint - " + sept
        # ISSUES WITH SEPTUAGINT TRY GENESIS 1:1 ALSO SOME JEREMIAH VERSES FOR EXAMPLE - LOOK INTO JSON FILE -
        # json showing first index as "\ufeffGenesis 1:1" - that's the issue

        # BEREAN
        try:
            bi = self.berean_search(searchText)
            bi_index0 = berean[bi]
            bi_index1 = berean[bi + 1]
            bi_index2 = berean[bi + 2]
            bi_index3 = berean[bi + 3]
            bi_index4 = berean[bi + 4]
            bereanLabel = bi_index0\
                  + '\nBGB (Berean Greek Bible) - ' + bi_index1\
                  + '\n\nBIB (Berean Interlinear Bible) - ' + bi_index2\
                  + '\n\nBLB (Berean Literal Bible) - ' + bi_index3\
                  + '\n\nBSB (Berean Study Bible) - ' + bi_index4 + '\n\n'

        except:
            bereanLabel = "Berean Bible - No verse found in the Berean Bible for your search..."

        # GET TWI SCRIPTURE INDEX
        try:
            twi = self.twi_scripture_index(searchText)
            twiLabel = "Scripture Index : \n" + ' '.join(twi)
        except:
            twiLabel = "Nothing found in Scripture Index for your search..."

        # GET ALL GREEK AND HEBREW DEFINITIONS HERE...
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

        return kjvLabel + '\n\n' + kjvsLabel + '\n\n' + strongsDefinitions\
             + '\n\n' + septLabel + '\n\n' + bereanLabel + '\n\n' + twiLabel

    # Retrieve text from searchBox
    def getSearchBox(self):
        retrieved = self.searchBox.text()
        self.searchBox.setText('')
        return retrieved     

    # Retrieve text from TextSearchBox
    def getTextSearchBox(self):
        retrieved = self.textSearchBox.text()
        self.textSearchBox.setText('')
        return retrieved

    # A METHOD TO CLEAR ALL TEXT
    def clearTxt(self):
        self.textEditor.clear()
    
    # Radio button search for searchToolbar
    def radioSearch(self):

        if self.radioButtonBerean.isChecked():
            
            bi = self.berean_search(self.getSearchBox())
            bi_index0 = berean[bi]
            bi_index1 = berean[bi + 1]
            bi_index2 = berean[bi + 2]
            bi_index3 = berean[bi + 3]
            bi_index4 = berean[bi + 4]
            bereanLabel = bi_index0\
                  + '\nBGB (Berean Greek Bible) - ' + bi_index1\
                  + '\n\nBIB (Berean Interlinear Bible) - ' + bi_index2\
                  + '\n\nBLB (Berean Literal Bible) - ' + bi_index3\
                  + '\n\nBSB (Berean Study Bible) - ' + bi_index4 + '\n\n'
            self.textUpdate(bereanLabel)

        elif self.radioButtonKJV.isChecked():
            returnedVerses = self.kjv_search(self.getSearchBox())
        
            for verse in returnedVerses:
                self.textUpdate(verse)
        
        elif self.radioButtonKJVwStrongs.isChecked():
            searchText = self.getSearchBox()
            try:
                kjvs = self.kjvstrnumOT_search(searchText)
            except:
                kjvs = self.kjvstrnumNT_search(searchText)
            kjvsLabel = "KJV w/Strong's - " + ' - '.join(kjvs)
            self.textUpdate(kjvsLabel)
        
        elif self.radioButtonScriptureIndex.isChecked():
            try:
                twi = self.twi_scripture_index(self.getSearchBox())
                twiLabel = "Scripture Index : \n" + ' '.join(twi)
            except:
                twiLabel = "Nothing found in Scripture Index for your search..."
            self.textUpdate(twiLabel)
        
        elif self.radioButtonSearchAll.isChecked():
            self.textUpdate(self.searchAll(self.getSearchBox()))
        
        elif self.radioButtonSeptuagint.isChecked():
            try:
                sept = self.septuagint_search(self.getSearchBox())    
                septLabel = "Septuagint - " + ' - '.join(sept)
            except:
                sept = "No verse found in Septuagint for your search..."
                septLabel = "Septuagint - " + sept
            self.textUpdate(septLabel)
        
        else:
            self.textUpdate(self.searchAll(self.getSearchBox()))

    # Radio button search for greekHebrew
    def greekHebrewRadioSearch(self):

        retrieved = self.searchHebrewGreekBox.text()
        self.searchHebrewGreekBox.setText('')

        retrieved = retrieved.upper()

        if self.radioButtonHebrew.isChecked():

            if 'H' in retrieved:
                pass
            else:
                retrieved = 'H' + retrieved

            try:
                sc = self.strongs_search(retrieved)
                sc_index0 = strongscsvlst[sc]
                sc_index1 = strongscsvlst[sc + 1]
                sc_index2 = strongscsvlst[sc + 2]
                sc_index3 = strongscsvlst[sc + 3]
                sc_index4 = strongscsvlst[sc + 4]
                sc_index5 = strongscsvlst[sc + 5]
                sc_index6 = strongscsvlst[sc + 6]
                txt = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                      + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                      ' ' + sc_index5 + ', ' + sc_index6)
                self.textUpdate(txt)

            except:
                self.textUpdate("No Hebrew definitions found for your search.")

        elif self.radioButtonGreek.isChecked():
            
            if 'G' in retrieved:
                pass
            else:
                retrieved = 'G' + retrieved

            try:
                sc = self.strongs_search(retrieved)
                sc_index0 = strongscsvlst[sc]
                sc_index1 = strongscsvlst[sc + 1]
                sc_index2 = strongscsvlst[sc + 2]
                sc_index3 = strongscsvlst[sc + 3]
                sc_index4 = strongscsvlst[sc + 4]
                sc_index5 = strongscsvlst[sc + 5]
                sc_index6 = strongscsvlst[sc + 6]
                txt = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                      + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                      ' ' + sc_index5 + ', ' + sc_index6)
                self.textUpdate(txt)

            except:
                self.textUpdate("No Greek definitions found for your search.")

# FOR WINDOW INSTEAD OF DIALOG SEE THIS - https://stackoverflow.com/questions/36768033/pyqt-how-to-open-new-window
#---------------------------------------------------------------------------------------------

    # Make a popup window asking where to save the file and what to name it
    # SEE THIS - https://pythonspot.com/pyqt5-file-dialog/
    # AND THIS - https://pythonprogramming.net/file-saving-pyqt-tutorial/
    # ** https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm **

    # NEW PROJECT
    #def newProject(self):

    # OPEN PROJECT
    def openProject(self):

        # load the txt file
        # code to load text file here...

        # load the notes dictionary from pickle file
        with open("notes_kjv.dat", 'rb') as f:
            notes_dictionary_kjv = cpickle.load(f)


    # SAVE PROJECT
    def saveProject(self):        

        # Write all text from QTextEdit (textEditor) to the text file
        with open("NewProject.txt", "w", encoding='utf-8') as txtFile:
            txtFile.write(self.textEditor.toPlainText())

        # save notes dictionary to a pickle file
        with open("notes_kjv.dat","wb") as f:
            cpickle.dump(notes_dictionary_kjv,f)
        
        f.close()


# ---------------------------------------------------------------------
# Run App
# ---------------------------------------------------------------------
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    simr = SIMR()
    sys.exit(app.exec_())


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# SEE - http://zetcode.com/gui/pyqt5/widgets2/
# SEE - https://www.tutorialspoint.com/pyqt/pyqt_qsplitter_widget.htm
# SEE - https://www.binpress.com/building-text-editor-pyqt-1/
# SEE - https://pythonbasics.org/pyqt-radiobutton/
# SEE - https://www.tutorialspoint.com/pyqt/pyqt_qradiobutton_widget.htm
# SEE - https://stackoverflow.com/questions/42288320/python-how-to-get-qlineedit-text?rq=1
# SEE - http://zetcode.com/gui/pyqt5/menustoolbars/

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# NEED TO BE ABLE TO ZOOM IN ON TEXT (OR CHANGE TEXT SIZE), AND ALSO MAP DIALOG ETC. - https://doc.qt.io/qt-5/qtextedit.html
# font sizes, color, etc. - https://www.binpress.com/building-text-editor-pyqt-2/

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# LOOK INTO MAKING WINDOWS DOCKABLE

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# ***REFACTOR CODE WHEN DONE - eliminate duplicate code in search functions***
