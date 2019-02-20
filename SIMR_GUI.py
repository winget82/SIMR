from tkinter import *
import tkinter.messagebox
import tempfile
import SIMR as s
import json

#-----------------------------------------------------------------------
#Make a temp blank icon on the fly (Windows) to get rid of tkinter feather
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)



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
myRoot = Tk()#THIS MAKES THE WINDOW THE MAIN ROOT WINDOW
myRoot.minsize(640,480)#set minimum size of window
myRootHeight = myRoot.winfo_height()#get window height
myRootWidth = myRoot.winfo_width()#get window width
myRoot.iconbitmap(default=ICON_PATH)#utilize blank icon to cover feather

#MAIN MENU
myMenu = Menu(myRoot)
myRoot.config(menu=myMenu)
myRoot.title("SIMR - Scripture Indices and Ministry Resources")

# File Menu
fileMenu = Menu(myMenu, tearoff=0)#tearoff gets rid of dashed line
myMenu.add_cascade(label="File", menu=fileMenu)#this adds a cascading (drop-down) menu
fileMenu.add_command(label="New Project", command=s.newProject)#command is set to a function
fileMenu.add_command(label="Save", command=s.saveProject)
fileMenu.add_separator()#draws solid line seperator in cascading (drop-down)menu
fileMenu.add_command(label="Exit", command=s.exitApp)

# Edit Menu
editMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=s.undoAction)
editMenu.add_command(label="Redo", command=s.redoAction)

# Read various bibles
readMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Read", menu=readMenu)
readMenu.add_command(label="KJV")
readMenu.add_command(label="KJV w/ Strong's")
readMenu.add_command(label="Septuagint")
readMenu.add_command(label="Berean")

# Books (Reference Books - in public domain)
booksMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Books", menu=booksMenu)
booksMenu.add_command(label="Number in Scripture")
booksMenu.add_command(label="Witness of the Stars")
booksMenu.add_command(label="How to Enjoy the Bible")

# TWI Menu
twiMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="TWI", menu=twiMenu)
twiMenu.add_command(label="Scripture Index")
twiMenu.add_command(label="STS List")

# Help Menu
helpMenu = Menu(myMenu, tearoff=0)
myMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Documentation", command=s.documentation)

#TOOLBAR
myToolbar = Frame(myRoot)

kjvButton = Button(myToolbar, text="KJV", command=s.kjv)
kjvButton.pack(side=LEFT,padx=2, pady=2)#display button with padding of 2 pixels on either end of toolbar
kjvSButton = Button(myToolbar, text="KJV w/ Strong's", command=s.kjvs)
kjvSButton.pack(side=LEFT,padx=2, pady=2)
septButton = Button(myToolbar, text="Septuagint", command=s.sept)
septButton.pack(side=LEFT,padx=2, pady=2)
bereanButton = Button(myToolbar, text="Berean", command=s.berean)
bereanButton.pack(side=LEFT,padx=2, pady=2)
scriptIndexButton = Button(myToolbar, text="Scripture Index", command=s.scriptIndex)
scriptIndexButton.pack(side=LEFT,padx=2, pady=2)

myToolbar.pack(side=TOP, fill=X)#display the toolbar, fill=X makes the toolbar fill the x axis (Y would fill the Y axis - height)


#STATUS BAR AT BOTTOM
status = Label(myRoot, text="Displays your status here...", bd=1, relief=SUNKEN, anchor=E)#bd is border, anchor is East (makes text for the label on the left)
#try putting a function in the text part to see if you can get text to be dynamic
status.pack(side=BOTTOM, fill=X)#displays this at the bottom and at the width of the window


#HANDLE MOUSE EVENTS
#Make a frame / invisible widget to bind events to
myFrame = Frame(myRoot)
myFrame.bind("<Button-1>", s.leftClick)#bind the leftClick function to the left mouse button
myFrame.bind("<Button-2>", s.middleClick)#bind the middleClick function to the middle mouse button
myFrame.bind("<Button-3>", s.rightClick)#bind the rightClick function to the right mouse button
myFrame.pack(fill=BOTH, expand=True)#fill frame to window and make it expandable


#SAVE THIS FOR LAST
myRoot.mainloop()


# if you save this as .pyw then you can double click the icon and the
# python console window will be hidden
