# -*- coding: utf-8 -*-

#Program written by N. Flesher

"""Program for study of the scriptures"""

# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------

import re
import codecs
import json
from tkinter import Tk, Menu, Frame, Button, LEFT, StringVar, Entry, TOP, X, RIGHT, Label, SUNKEN, E, BOTTOM, BOTH, Scrollbar, Text, Y, WORD, END
#import tkinter
import ctypes
import time


#-----------------------------------------------------------------------
#Make a temp blank icon on the fly (WINDOWS ONLY) to get rid of tkinter feather
#ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
#        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
#        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64
#
#_, ICON_PATH = tempfile.mkstemp()
#with open(ICON_PATH, 'wb') as icon_file:
#    icon_file.write(ICON)


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

#MessageBox Function
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#WILL NEED TO USE TKINTER MESSAGE BOX / POP UP WINDOW INSTEAD - THIS DOESN'T WORK ON LINUX

#THIS SWEET FUNCTION ALLOWS YOU TO PASS TWO FUNCTIONS INTO ONE FUNCTION,
#ALLOWING YOU TO CALL MORE THAN ONE FUNCTION IN A TKINTER COMMAND ASSIGNMENT
def sequenceOfFunctions(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

#-----------------------------------------------------------------------
# WINDOW / APP
#-----------------------------------------------------------------------

class simrGUI:
    def __init__(self):
        
        #ROOT WINDOW
        self.myRoot = Tk()
        self.myRoot.minsize(640,480)
        #self.myRoot.iconbitmap(default=ICON_PATH)#utilize blank icon to cover feather

        self.projectName = 'New Project'

        #MAIN MENU
        self.myMenu = Menu(self.myRoot)
        self.myRoot.config(menu=self.myMenu)
        self.myRoot.title("SIMR - Scripture Indices and Ministry Resources")

        # File Menu
        self.fileMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="New Project", command=self.newProject)
        self.fileMenu.add_command(label="Save", command=self.saveProject)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitApp)

        # Edit Menu
        self.editMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Undo>>'), self.undoAction))
        self.editMenu.add_command(label="Redo", accelerator="Ctrl+Y", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Redo>>'), self.redoAction))
        #Control+Y not working for redo, it is pasting in

        # Read various bibles
        self.readMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="Read", menu=self.readMenu)
        self.readMenu.add_command(label="KJV")
        self.readMenu.add_command(label="KJV w/ Strong's")
        self.readMenu.add_command(label="Septuagint")
        self.readMenu.add_command(label="Berean")

        # Books (Reference Books - in public domain)
        self.booksMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="Books", menu=self.booksMenu)
        self.booksMenu.add_command(label="Number in Scripture")
        self.booksMenu.add_command(label="Witness of the Stars")
        self.booksMenu.add_command(label="How to Enjoy the Bible")

        # TWI Menu
        self.twiMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="TWI", menu=self.twiMenu)
        self.twiMenu.add_command(label="Scripture Index Abbreviations")
        self.twiMenu.add_command(label="STS List")

        # Help Menu
        self.helpMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="Documentation", command=self.documentation)
        self.helpMenu.add_command(label="Credits", command=self.getCredits)
        self.helpMenu.add_command(label="About", command=self.getAbout)

        #TOOLBAR
        self.myToolbar = Frame(self.myRoot)
        
        #KJV Button
        self.kjvButton = Button(self.myToolbar, text="KJV", command=self.kjvButtonT)
        self.kjvButton.pack(side=LEFT,padx=2, pady=2)

        #KJVS Button
        self.kjvSButton = Button(self.myToolbar, text="KJV w/ Strong's", command=self.kjvsButtonT)
        self.kjvSButton.pack(side=LEFT,padx=2, pady=2)
        
        #Septuagint Button
        self.septButton = Button(self.myToolbar, text="Septuagint", command=self.septButtonT)
        self.septButton.pack(side=LEFT,padx=2, pady=2)
        
        #Berean Button
        self.bereanButton = Button(self.myToolbar, text="Berean", command=self.bereanButtonT)
        self.bereanButton.pack(side=LEFT,padx=2, pady=2)

        #Hebrew Button
        self.hebrewButton = Button(self.myToolbar, text="Hebrew", command=self.hebrewButtonT)
        self.hebrewButton.pack(side=LEFT,padx=2, pady=2)

        #Greek Button
        self.greekButton = Button(self.myToolbar, text="Greek", command=self.greekButtonT)
        self.greekButton.pack(side=LEFT,padx=2, pady=2)

        #Scripture Index Button
        self.scriptIndexButton = Button(self.myToolbar, text="Scripture Index", command=self.scriptIndexButtonT)
        self.scriptIndexButton.pack(side=LEFT,padx=2, pady=2)
        
        #Text Entry Box
        self.entryText = StringVar(self.myToolbar)
        #self.entryText.set("")
        self.searchBox = Entry(self.myToolbar, textvariable=self.entryText)
        self.searchBox.pack(side=LEFT, padx=2, pady=2)
        
        #Search Button
        self.searchButton = Button(self.myToolbar, text="Search All", command=self.searchAll)
        self.searchButton.pack(side=LEFT,padx=2, pady=2)
        self.searchBox.bind('<Return>', self.searchAll)
        
        #Clear Button
        self.clearButton = Button(self.myToolbar, text="[X]", command=self.clearTxt, fg="red")
        self.clearButton.pack(side=RIGHT, padx=2, pady=2)

        #Pack the Toolbar
        self.myToolbar.pack(side=TOP, fill=X)

        #STATUS BAR AT BOTTOM
        self.statusBar = Label(self.myRoot, text="Displays your status here...", bd=1, relief=SUNKEN, anchor=E)
        #try putting a function in the text part to see if you can get text to be dynamic
        #SEE - https://www.youtube.com/watch?v=Mhwiy8Tr6Wo&index=13&list=PLhTjy8cBISEp6lNKUO3iwbB1DKAkRwutl&t=0s
        self.statusBar.pack(side=BOTTOM, fill=X)#displays this at the bottom and at the width of the window


        #FRAME
        self.myFrame = Frame(self.myRoot)
        self.myFrameText = ''
        self.myFrame.pack(fill=BOTH, expand=True)            
        self.myFrame.update()


        #SCROLLBAR & TEXT WIDGET
        self.scrollbar = Scrollbar(self.myFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.textOut = Text(self.myFrame, wrap=WORD, undo=True, autoseparators=True, maxundo=-1)
        self.textOut.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrollbar.config(command=self.textOut.yview)
        self.textOut.config(yscrollcommand=self.scrollbar.set)
        self.textOut.insert(END, self.myFrameText)
        self.textOut.bind("<Button-1>", self.leftClick)
        self.textOut.bind("<Button-2>", self.middleClick)
        self.textOut.bind("<Button-3>", self.rightClick)
        #https://www.python-course.eu/tkinter_text_widget.php
        #https://www.tutorialspoint.com/python/tk_text.htm
        # *** http://effbot.org/tkinterbook/text.htm *** THIS IS DETAILED DO NOT DELETE


        #RIGHT CLICK MENU
        self.rClickMenu = Menu(self.myFrame, tearoff=0)
        self.rClickMenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.textOut.focus_get().event_generate('<<Copy>>'))
        self.rClickMenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.textOut.focus_get().event_generate('<<Cut>>'))
        self.rClickMenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.textOut.focus_get().event_generate('<<Paste>>'))
        self.rClickMenu.add_command(label="Greek", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Copy>>'), self.rightClickGreekSearch))
        self.rClickMenu.add_command(label="Hebrew", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Copy>>'), self.rightClickHebrewSearch))
        self.rClickMenu.add_command(label="Search All", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Copy>>'), self.rightClickSearch))
        self.rClickMenu.add_command(label="Bible Dict.", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Copy>>'), self.rightClickSearch))
        self.rClickMenu.add_command(label="Find Text", command=sequenceOfFunctions(lambda: self.textOut.focus_get().event_generate('<<Copy>>'), self.rightClickFindTxt))
        self.rClickMenu.add_command(label="Clear", command=self.clearTxt)
        self.rClickMenu.add_command(label="Close Menu")


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


        #MAIN LOOP FOR TKINTER
        self.myRoot.mainloop()


        # if you save this as .pyw then you can double click the icon and the
        # python console window will be hidden


    # /////////////////////////////////////////////////////////////////////
    # METHODS OF THE SIMRGUI CLASS
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    #-----------------------------------------------------------------------
    # Search Methods
    #-----------------------------------------------------------------------

    # WRITE A FUNCTION TO SEARCH FOR WORD OR PHRASE TYPED OR SELECTED (RIGHT CLICK MENU)
    # AND RETURN LIST OF VERSES CONTAINING THE SEARCH STRING
    def find_txt(self,text):
        #returnedVerses = []
        #need to change text into a regex - right now I think there is formatting captured in the i[1]
        #that is preventing from returning the verse.  It'll return the verse if you search by John 1:1
        #but not by the text of the verse.  This method returns the entire list for the match
        # when scriptures_lst = [['abc', '123'], ['def', '345'], ['ewr', '345']]
        # print(find_txt("345"))
        # ['def', '345'] is returned
        # will also need to determine how to get it to pull each match throughout the entire bible
        # not just the first match it finds - figure out how to use a regex to do this
        # also will want to do this for each bible version

        found = next(i for i in scriptures_lst if text in i)
        return found
        
        # try https://stackoverflow.com/questions/33938488/finding-the-index-of-an-element-in-nested-lists-in-python
        #return kjvtxt, kjvstext, septtext, bereantext

    # Search KJV verse
    def kjv_search(self, verse):#CAN SEARCH FOR A LIST OF VERSES TYPED LIKE JOHN 1:1, aCTS 2:4, james 1:1
        returnedVerses = []
        verses = verse.split(',')
        for v in verses:
            v = v.strip()
            found = next(i for i in scriptures_lst if v in i)
            returnedVerses.append(' '.join(found))
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


    #-----------------------------------------------------------------------
    # MENU METHODS
    #-----------------------------------------------------------------------

    # METHOD FOR TESTING PURPOSES
    def showIt(self):
        print("This button works...")

    # NEW PROJECT
    def newProject(self):
        print("New Project...")
        self.statusBar['text'] = "Starting new project..."

    # SAVE PROJECT
    def saveProject(self):
        with open("NewProject.txt", "w", encoding='utf-8') as txtFile:
            txtFile.write(self.getAllText())
        print("Saving...")
        self.statusBar['text'] = "Saving..."
        #NEED TO ADD A POPUP WINDOW THAT ASKS FOR FILE NAME AND FILEPATH LOCATION TO SAVE THE FILE
        #FIX ENCODING - SEE OLD SIMR PROGRAM FOR ENCODINGS TO COPY OVER FOR WRITING TO TEXT FILE

    # EXIT APP
    def exitApp(self):
        print("Exiting...")
        self.statusBar['text'] = "Exiting..."
        exit()

    # REDO - FOR UPDATING STATUS BAR ONLY
    def redoAction(self):
        print("Redoing...")
        self.statusBar['text'] = "Redoing previous action..."

    # UNDO - FOR UPDATING STATUS BAR ONLY
    def undoAction(self):
        print("Undoing...")
        self.statusBar['text'] = "Undoing last action..."

    # GET DOCUMENTATION
    def documentation(self):
        print("Getting documentation...")
        self.statusBar['text'] = "Getting documentation..."

    # GET KJV
    def kjv(self):
        print("Getting King James Version...")
        self.statusBar['text'] = "Getting the King James Version text..."

    # GET KJVS
    def kjvs(self):
        print("Getting King James Version with Strong's...")
        self.statusBar['text'] = "Getting the King James Version text with Strong's Numbers..."

    # GET SEPTUAGINT
    def sept(self):
        print("Getting Septuagint...")
        self.statusBar['text'] = "Getting the Septuagint text..."

    # GET BEREAN
    def berean(self):
        print("Getting Berean...")
        self.statusBar['text'] = "Getting the Berean texts..."

    # GET SCRIPTURE INDEX
    def scriptIndex(self):
        print("Getting Scripture Index...")
        self.statusBar['text'] = "Getting The Way International resources scripture index..."

    # GET ABOUT INFO
    def getAbout(self):
        Mbox('About', self.about, 0)
        self.statusBar['text'] = "Getting about information..."

    # GET CREDITS INFO
    def getCredits(self):
        Mbox('Credits', self.credits, 0)
        self.statusBar['text'] = "Getting credits..."


    #-----------------------------------------------------------------------
    # TOOLBAR METHODS
    #-----------------------------------------------------------------------


    #search button on toolbar
    def searchAll(self, event=None):#ONLY WORKS WHEN SEARCHING FOR ONE VERSE AT A TIME BECAUSE ONLY KJV IS SET UP TO SEARCH FOR LIST OF VERSES SEPARATED BY A COMMA
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Gathering all resources for you..."
        
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

        self.update_textOut(kjvLabel + '\n\n' + kjvsLabel + '\n\n' + strongsDefinitions + '\n\n' + septLabel + '\n\n' + twiLabel)

    #FOR KJV BUTTON
    def kjvButtonT(self, event=None):#CAN NOW SEARCH FOR MORE THAN ONE VERSE WHEN VERSES ARE SEPARATED BY A COMMA
        print("Getting King James Version...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting KJV..."

        try:
            txt = self.kjv_search(searchText)
            self.update_textOut("KJV:\n" + '\n\n'.join(txt))
            print(txt)
            return "KJV:\n" + '\n\n'.join(txt)
        except:
            self.update_textOut("No verse found in the King James Version for your search.")

    #FOR KJV W/STRONGS BUTTON
    def kjvsButtonT(self, event=None):
        print("Getting King James Version with Strong's...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting KJV w/Strong's Numbers..."
        
        try:
            ot = self.kjvstrnumOT_search(searchText)
            self.update_textOut("KJV w/ Strong's - " + ' - '.join(ot))
            print(ot)
            return "KJV w/ Strong's - " + ' - '.join(ot)
            
        except:
            nt = self.kjvstrnumNT_search(searchText)
            self.update_textOut("KJV w/ Strong's - " + ' - '.join(nt))
            print(nt)
            return "KJV w/ Strong's - " + ' - '.join(nt)

    #FOR SEPTUAGINT BUTTON
    def septButtonT(self, event=None):
        print("Getting Septuagint...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting Septuagint..."

        try:
            txt = self.septuagint_search(searchText)
            self.update_textOut("Septuagint - " + ' - '.join(txt))
            print(txt)
            return "Septuagint - " + ' - '.join(txt)
        except:
            txt = "No verse found in Septuagint for your search."
            self.update_textOut("Septuagint - " + txt)
            print(txt)
            return "Septuagint - " + txt
        
    #FOR BEREAN BUTTON
    def bereanButtonT(self, event=None):
        print("Getting Berean...")
    #    searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting Berean Bible..."
    #    txt = 
    #    self.update_textOut(searchText)
    #    print("Berean - " + searchText)

    #FOR SCRIPTURE INDEX BUTTON
    def scriptIndexButtonT(self, event=None):
        print("Getting Scripture Index...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting The Way International resources scripture index..."

        try:
            txt = self.twi_scripture_index(searchText)
            self.update_textOut("Scripture Index : \n" + ' '.join(txt))
            print(txt)
        except:
            self.update_textOut("No verse found in Scripture index for your search.")

    #FOR HEBREW BUTTON
    def hebrewButtonT(self, event=None):
        print("Getting Hebrew definitions...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting Strong's Hebrew definition..."

        try:
            sc = self.strongs_search(searchText)
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
            self.update_textOut(txt)
            print(txt)
        except:
            self.update_textOut("No Hebrew definitions found for your search.")

    #FOR GREEK BUTTON
    def greekButtonT(self, event=None):
        print("Getting Greek definitions...")
        searchText = self.searchBox.get().title()
        self.searchBox.delete(0, END)
        self.statusBar['text'] = "Getting Strong's Greek definition..."

        try:
            sc = self.strongs_search(searchText)
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
            self.update_textOut(txt)
            print(txt)
        except:
            self.update_textOut("No Greek defintions found for your search.")


    #NEED TO MAKE A FUNCTION TO SEARCH FOR GREEK WORDS BY GREEK CHARACTERS YOU CAN COPY AND PASTE FROM STRONGS
    #ALSO ONE FOR HEBREW

    #NEED TO ADD A SEARCH FUNCTION TO PULL ALL GREEK DEFINITIONS IN WHEN YOU HIT GREEK BUTTON WITH A VERSE TYPED IN
    #NEED TO ADD A SEARCH FUNCTION TO PULL ALL HEBREW DEFINITIONS IN WHEN YOU HIT GREEK BUTTON WITH A VERSE TYPED IN


    #-----------------------------------------------------------------------
    #HANDLE MOUSE EVENTS METHODS
    #-----------------------------------------------------------------------

    #RIGHT CLICK SEARCH ALL FUNTION - TO SEARCH FOR ALL INFORMATION ABOUT SELECTED VERSE REFERENCE TEXT
    def rightClickSearch(self, event=None):
        searchText = self.textOut.clipboard_get().title().strip()
        self.statusBar['text'] = "Gathering all resources for you..."
        
        #GET KJV
        try:
            kjv = self.kjv_search(searchText)
            kjvLabel = "KJV:\n" + '\n\n'.join(kjv)
        except:
            pass
        
        #GET KJV W/STRONGS
        try:
            try:
                kjvs = self.kjvstrnumOT_search(searchText)
            except:
                kjvs = self.kjvstrnumNT_search(searchText)
            kjvsLabel = "KJV w/Strong's - " + ' - '.join(kjvs)
        except:
            pass
        
        #GET SEPTUAGINT
        try:
            try:
                sept = self.septuagint_search(searchText)    
                septLabel = "Septuagint - " + ' - '.join(sept)
            except:
                sept = "No verse found in Septuagint for your search..."
                septLabel = "Septuagint - " + sept
            #ISSUES WITH SEPTUAGINT TRY GENESIS 1:1 ALSO SOME JEREMIAH VERSES FOR EXAMPLE - LOOK INTO JSON FILE -
            # json showing first index as "\ufeffGenesis 1:1" - that's the issue
        except:
            pass

        #berean = self.
        #bereanLabel = 

        #GET TWI SCRIPTURE INDEX
        try:
            try:
                twi = self.twi_scripture_index(searchText)
                twiLabel = "Scripture Index : \n" + ' '.join(twi)
            except:
                twiLabel = "Nothing found in Scripture Index for your search..."
        except:
            pass

        try:
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
        except:
            pass

        #NEED TO THINK THIS THROUGH BETTER (BELOW TRY/EXCEPT NESTED TRY/EXCEPT) - MAY NEED TO USE IF ELIF ELSE STATEMENT TO DETERMINE WHICH
        #self.update_textOut() HAPPENS.  BECAUSE THIS IS PULLING HEBREW, WHICH SHOULD PULL GREEK FIRST...???
        #That is because of (see lines 721 to 733 above) H# being generated skipping the except statement to generate a G#
        try:
            self.update_textOut(kjvLabel + '\n\n' + kjvsLabel + '\n\n' + strongsDefinitions + '\n\n' + septLabel + '\n\n' + twiLabel)
        except:
            pass

    # RIGHT CLICK SEARCH FOR GREEK DEFINITION OF SELECTED TEXT NUMBER
    def rightClickGreekSearch(self, event=None):
        searchText = self.textOut.clipboard_get().title()
        self.statusBar['text'] = "Getting Greek word and definition for you..."
        
        try:
            sc = self.strongs_search('G' + searchText)
            sc_index0 = strongscsvlst[sc]
            sc_index1 = strongscsvlst[sc + 1]
            sc_index2 = strongscsvlst[sc + 2]
            sc_index3 = strongscsvlst[sc + 3]
            sc_index4 = strongscsvlst[sc + 4]
            sc_index5 = strongscsvlst[sc + 5]
            sc_index6 = strongscsvlst[sc + 6]
            gTxt = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                  + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                  ' ' + sc_index5 + ', ' + sc_index6)
            print(gTxt)
            self.update_textOut(gTxt)    
        except:
            pass     

    # RIGHT CLICK SEARCH FOR HEBREW DEFINITION OF SELECTED TEXT NUMBER
    def rightClickHebrewSearch(self, event=None):
        searchText = self.textOut.clipboard_get().title()
        self.statusBar['text'] = "Getting Hebrew word and definition for you..."
        
        try:
            sc = self.strongs_search('H' + searchText)
            sc_index0 = strongscsvlst[sc]
            sc_index1 = strongscsvlst[sc + 1]
            sc_index2 = strongscsvlst[sc + 2]
            sc_index3 = strongscsvlst[sc + 3]
            sc_index4 = strongscsvlst[sc + 4]
            sc_index5 = strongscsvlst[sc + 5]
            sc_index6 = strongscsvlst[sc + 6]
            hTxt = ('\n' + sc_index0 + ' - ' + sc_index1 + ' - '
                  + sc_index2 + ' (' + sc_index3 + ') ' + sc_index4 +
                  ' ' + sc_index5 + ', ' + sc_index6)
            print(hTxt)
            self.update_textOut(hTxt)
        except:
            pass

    def rightClickFindTxt(self, event=None):#THIS IS NOT WORKING THE WAY I WANT
        self.statusBar['text'] = "Searching for text phrase..."
        searchText = self.textOut.clipboard_get().title().strip()
        final = self.find_txt(searchText)
        print(final)
        self.update_textOut(' - '.join(final))
                

    def leftClick(self, event):
        print("Left")
        #make selection here, etc

    def middleClick(self, event):
        print("Middle")
        
    def rightClick(self, event):
        print("Right")
        self.rClickMenu.post(event.x_root, event.y_root)


    #-----------------------------------------------------------------------
    #TEXT WIDGET METHODS
    #-----------------------------------------------------------------------

    # UPDATES THE TEXT ON THE TEXT WIDGET - should probably rename myFrameText to myTextOutText or something
    def update_textOut(self, text):
        self.myFrameText = text + '\n\n'
        self.textOut.insert(END, self.myFrameText)

    # NEED A METHOD TO CLEAR ALL TEXT
    def clearTxt(self):
        self.textOut.delete(1.0, END)
        self.statusBar['text'] = "Clearing all text..."

    # COLLECTS ALL TEXT IN THE TEXT WIDGET TO A VARIABLE - USED TO SAVE FILE
    def getAllText(self):
        contents = self.textOut.get("1.0", "end-1c")
        print("Getting all text...")
        return contents


#-----------------------------------------------------------------------
#RUN THE PROGRAM
#-----------------------------------------------------------------------

simrGUI = simrGUI()


#-----------------------------------------------------------------------
#MISC NOTES / REFERENCES
#-----------------------------------------------------------------------

#https://www.delftstack.com/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/
#https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
#https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python

#MAKE GIS MAP BIBLE ATLAS - if you use leaflet see the faq about crediting them
#SEE - https://programminghistorian.org/en/lessons/mapping-with-python-leaflet
#SEE - https://leafletjs.com/
#see also Folium and if it is opensource and no fee - https://www.youtube.com/watch?v=xN2N-p33V1k

#ATTACH POEMS, SONGS, TEACHINGS / MP3s, REFERENCE MATERIALS IN THE PUBLIC DOMAIN
