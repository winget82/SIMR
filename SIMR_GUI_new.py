# -*- coding: utf-8 -*-

#Program written by N. Flesher

"""Program for study of the scriptures"""

# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QLineEdit, QTextEdit, QSplitter, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
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

        # SEE - https://www.tutorialspoint.com/pyqt/pyqt_qsplitter_widget.htm
        # SEE - https://www.binpress.com/building-text-editor-pyqt-1/

        # File Menu Options
        newProject = QAction(QIcon('./toolbar_icons/iconfinder_document_basic_blue_69485.png'), '&New Project', self)
        newProject.setStatusTip('Start a new project')
        
        openProject = QAction(QIcon('./toolbar_icons/iconfinder_folder_basic_blue_69500.png'), '&Open Project', self)
        openProject.setStatusTip('Open an existing project')

        saveProject = QAction(QIcon('./toolbar_icons/iconfinder_floppy-disk_basic_yellow_70075.png'), '&Save Project', self)        
        saveProject.setStatusTip('Save your current project')
        #saveApp.triggered.connect()

        closeApp = QAction(QIcon('./toolbar_icons/iconfinder_archive_basic_blue_69430.png'), '&Exit', self)        
        closeApp.setStatusTip('Close and exit SIMR')
        closeApp.triggered.connect(qApp.quit)

        # Edit Menu Options
        undoAction = QAction(QIcon('./toolbar_icons/iconfinder_arrow-left_basic_red_69816.png'), '&Undo', self)
        undoAction.setStatusTip('Undo your last action')

        redoAction = QAction(QIcon('./toolbar_icons/iconfinder_arrow-right_basic_yellow_70009.png'), '&Redo', self)
        redoAction.setStatusTip('Redo your last action')

        appSettings = QAction(QIcon('./toolbar_icons/iconfinder_gears_basic_green_69695.png'), '&Settings', self)
        appSettings.setStatusTip('View and adjust your settings')

        # Search Menu Options
        searchAll = QAction(QIcon('./toolbar_icons/iconfinder_search_basic_blue_69571.png'), '&Search All', self)
        searchAll.setStatusTip('Search through all resources')

        # Read Menu Options
        readKJV = QAction('&King James Version', self)
        readKJV.setStatusTip('Read from the King James Version')

        readKJVwStrongs = QAction("&KJV w/ Strong's", self)
        readKJVwStrongs.setStatusTip("Read from the KJV with Strong's numbers")

        readSept = QAction('&Septuagint', self)
        readSept.setStatusTip('Read from the Septuagint')

        readBerean = QAction('&Berean', self)
        readBerean.setStatusTip('Read from the Berean Bible')

        # Books Menu Options
        numberInScripture = QAction('&Number In Scripture', self)
        numberInScripture.setStatusTip('Read from "Number in Scripture" by E. W. Bullinger')

        howToEnjoyTheBible = QAction('&How To Enjoy The Bible', self)
        howToEnjoyTheBible.setStatusTip('Read from "How to Enjoy the Bible" by E. W. Bullinger')

        witnessOfTheStars = QAction('&Witness Of The Stars', self)
        witnessOfTheStars.setStatusTip('Read from "Witness of the Stars" by E. W. Bullinger')

        # TWI Menu Options
        scriptureIndex = QAction('&Scripture Index', self)
        scriptureIndex.setStatusTip('Get scripture index for The Way International resources')

        # Scripture Bank Menu Options
        visitScriptureBank = QAction(QIcon('./toolbar_icons/iconfinder_bank_basic_red_69821.png'), '&Visit Scripture Bank', self)
        visitScriptureBank.setStatusTip('Visit your Scripture Bank')
        depositVerse = QAction('&Deposit Verse', self)
        depositVerse.setStatusTip('Deposit a verse into your Scripture Bank')
        checkBalance = QAction('&Check Balance', self)
        checkBalance.setStatusTip('Check you Scripture Bank account balance')
        withdrawVerse = QAction('&Withdraw Verse', self)
        withdrawVerse.setStatusTip('Withdraw a verse from your Scripture Bank')

        # Mapping Menu Options
        drawMap = QAction(QIcon('./toolbar_icons/iconfinder_compass_basic_blue_69477.png'), 'Draw Map', self)
        drawMap.setStatusTip('Draw Bible map')

        # Help Menu Options
        aboutApp = QAction(QIcon('./toolbar_icons/iconfinder_information_basic_green_69706.png'), 'About', self)
        aboutApp.setStatusTip('See information about this application')

        appDocumentation = QAction(QIcon('./toolbar_icons/iconfinder_question_basic_green_69755.png'), 'Documentation', self)
        appDocumentation.setStatusTip('See documentation about using this application')

        creditsThanks = QAction('Credits / Thanks', self)
        creditsThanks.setStatusTip('See credits and special thanks')

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
        editMenu.addAction(undoAction)
        editMenu.addAction(redoAction)
        editMenu.addAction(appSettings)

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
        self.mainToolbar.addAction(undoAction)
        self.mainToolbar.addAction(redoAction)
        self.mainToolbar.addAction(appSettings)
        self.mainToolbar.addAction(visitScriptureBank)
        self.mainToolbar.addAction(drawMap)
        self.mainToolbar.addAction(appDocumentation)
        self.mainToolbar.addAction(aboutApp)

        # Search Toolbar
        self.searchToolbar = self.addToolBar('Search Toolbar')
        self.searchToolbar.addAction(searchAll)
        self.searchBox = QLineEdit(self.searchToolbar)
        self.searchBox.move(50, 7)
        self.searchBox.resize(150, 25)


        # SEE - http://zetcode.com/gui/pyqt5/menustoolbars/

        self.setGeometry(600, 600, 600, 400)
        self.setWindowTitle('SIMR - Scripture Indices and Ministry Resources')    
        self.show()
    

    def buttonClick(self):
        alert = QMessageBox()
        alert.setText('Button has been clicked')
        alert.exec_()

    
# ---------------------------------------------------------------------
# Run App
# ---------------------------------------------------------------------
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    simr = SIMR()
    sys.exit(app.exec_())


# ADD A SCRIPTURE BANK WHERE YOU CAN DEPOSIT AND WITHDRAW SCRIPTURES
