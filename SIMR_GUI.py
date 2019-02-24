# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------

import re
#from openpyxl import load_workbook
import codecs
import json
from tkinter import *


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


#-----------------------------------------------------------------------
# WINDOW / APP
#-----------------------------------------------------------------------

class simrGUI:
    def __init__(self):
        self.myRoot = Tk()
        self.myRoot.minsize(640,480)
        #self.myRoot.iconbitmap(default=ICON_PATH)#utilize blank icon to cover feather

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
        self.editMenu.add_command(label="Undo", command=self.undoAction)
        self.editMenu.add_command(label="Redo", command=self.redoAction)


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
        self.twiMenu.add_command(label="Scripture Index")
        self.twiMenu.add_command(label="STS List")

        # Help Menu
        self.helpMenu = Menu(self.myMenu, tearoff=0)
        self.myMenu.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="Documentation", command=self.documentation)

        #TOOLBAR
        self.myToolbar = Frame(self.myRoot)
        
        self.kjvButton = Button(self.myToolbar, text="KJV", command=self.kjv)
        self.kjvButton.pack(side=LEFT,padx=2, pady=2)
        self.kjvSButton = Button(self.myToolbar, text="KJV w/ Strong's", command=self.kjvs)
        self.kjvSButton.pack(side=LEFT,padx=2, pady=2)
        
        self.septButton = Button(self.myToolbar, text="Septuagint", command=self.sept)
        self.septButton.pack(side=LEFT,padx=2, pady=2)
        
        self.bereanButton = Button(self.myToolbar, text="Berean", command=self.berean)
        self.bereanButton.pack(side=LEFT,padx=2, pady=2)
        
        self.scriptIndexButton = Button(self.myToolbar, text="Scripture Index", command=self.scriptIndex)
        self.scriptIndexButton.pack(side=LEFT,padx=2, pady=2)
        
        self.entryText = StringVar(self.myToolbar)
        self.entryText.set("Search...")
        self.searchBox = Entry(self.myToolbar, textvariable=self.entryText)
        self.searchBox.pack(side=LEFT, padx=2, pady=2)
        self.searchButton = Button(self.myToolbar, text="Search", command=self.search)
        self.searchButton.pack(side=LEFT,padx=2, pady=2)
        self.searchBox.bind('<Return>', self.search)
        self.myToolbar.pack(side=TOP, fill=X)


        #STATUS BAR AT BOTTOM
        self.status = Label(self.myRoot, text="Displays your status here...", bd=1, relief=SUNKEN, anchor=E)
        #try putting a function in the text part to see if you can get text to be dynamic
        self.status.pack(side=BOTTOM, fill=X)#displays this at the bottom and at the width of the window


        #HANDLE MOUSE EVENTS
        #Make a frame / invisible widget to bind events to
        self.myFrame = Frame(self.myRoot)
        self.myFrame.bind("<Button-1>", self.leftClick)
        self.myFrame.bind("<Button-2>", self.middleClick)
        self.myFrame.bind("<Button-3>", self.rightClick)
        self.myFrame.pack(fill=BOTH, expand=True)
        
        self.returnedText = 'Display returned text on frame'
        
        #LABEL FOR TEXT OUTPUT
        self.textOut = Label(self.myFrame, text=self.returnedText)
        self.textOut.pack(side=TOP, anchor=W)
        
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

    # Search KJV verse
    def kjv_search(self, verse):
        #found = next(i for i in scriptures_lst if kjv_inp in i)
        found = next(i for i in scriptures_lst if verse in i)
        return found

    # Search KJV w/ Strong's verse
    def kjvstrnumOT_search(self, searchOT_ks):
        found_snOT = next(i for i in OT_sn if searchOT_ks in i)
        return found_snOT

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
    def strongs_search(self):
        inp = input("Enter Strong's Number proceeded by CAPITAL G or H: ")
        if inp in strongscsvlst:
            sc = strongscsvlst.index(inp)  # This is based on verse seached for.
            # Sets sc to the strongs number searched for
            return sc

    # OT Hebrew Strong's Definitions Search
    def strnumOT(self, OTsearch):
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

    def get_strhebdefs(self, SNH):
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
    def strnumNT(self, NTsearch):
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

    def get_strgredefs(self, SNG):
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


    #-----------------------------------------------------------------------
    # MENU FUNCTIONS
    #-----------------------------------------------------------------------

    def showIt(self):
        print("This button works...")

    def newProject(self):
        print("New Project...")

    def saveProject(self):
        print("Saving...")

    def exitApp(self):
        print("Exiting...")

    def redoAction(self):
        print("Redoing...")

    def undoAction(self):
        print("Undoing...")

    def documentation(self):
        print("Getting documentation...")

    def kjv(self):
        print("Getting King James Version...")

    def kjvs(self):
        print("Getting King James Version with Strong's...")

    def sept(self):
        print("Getting Septuagint...")

    def berean(self):
        print("Getting Berean...")

    def scriptIndex(self):
        print("Getting Scripture Index...")


    #-----------------------------------------------------------------------
    # TOOLBAR FUNCTIONS
    #-----------------------------------------------------------------------

    def outText(self, text):
        print(text)

    #search button on toolbar
    def search(self, event=None):
            searchText = self.searchBox.get()
            print(searchText)
            return searchText


    #-----------------------------------------------------------------------
    #HANDLE MOUSE EVENTS (FUNCTIONS)
    #-----------------------------------------------------------------------

    def leftClick(self, event):
        print("Left")

    def middleClick(self, event):
        print("Middle")

    def rightClick(self, event):
        print("Right")


#-----------------------------------------------------------------------
#RUN THE PROGRAM
#-----------------------------------------------------------------------

simrGUI = simrGUI()


#-----------------------------------------------------------------------
#MISC NOTES / REFERENCES
#-----------------------------------------------------------------------

#https://www.delftstack.com/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/
#LOOK INTO THIS FOR UPDATING TEXT ON THE FRAME AFTER SUBMITTING TEXT IN SEARCH BOX
#https://www.daniweb.com/programming/software-development/threads/312235/refresh-canvas-in-tkinter
#https://stackoverflow.com/questions/17125842/changing-the-text-on-a-label
#LOOK INTO TKINTER'S .trace_variable() to update text on frames