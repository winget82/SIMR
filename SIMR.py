"""These are functions to import for SIMR GUI"""

# ---------------------------------------------------------------------
# IMPORTS - PACKAGES & MODULES UTILIZED
# ---------------------------------------------------------------------
import re
#from openpyxl import load_workbook
import codecs
import json


# /////////////////////////////////////////////////////////////////////
# FUNCTIONS / METHODS
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#-----------------------------------------------------------------------
# Search Functions
#-----------------------------------------------------------------------

# Search KJV verse function
def kjv_search(verse):
    #found = next(i for i in scriptures_lst if kjv_inp in i)
    found = next(i for i in scriptures_lst if verse in i)
    return found

# Search KJV w/ Strong's verse functions
def kjvstrnumOT_search(searchOT_ks):
    found_snOT = next(i for i in OT_sn if searchOT_ks in i)
    return found_snOT

def kjvstrnumNT_search(searchNT_ks):
    found_snNT = next(i for i in NT_sn if searchNT_ks in i)
    return found_snNT

# Search for Berean verses function
def berean_search(berean_inp):
    if berean_inp in berean:
        bi = berean.index(berean_inp)  # This is based on verse seached for.
        # Sets bi to the index of verse searched for
        return bi

# Search through TWI scripture index function
def twi_scripture_index(twi_inp):
    found2 = next(i for i in twi_index if twi_inp in i)
    return found2

# Search through septuagint function
def septuagint_search(sept_inp):
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


#-----------------------------------------------------------------------
# MENU FUNCTIONS
#-----------------------------------------------------------------------

def showIt():
    print("This button works...")

def newProject():
    print("New Project...")

def saveProject():
    print("Saving...")

def exitApp():
    print("Exiting...")

def redoAction():
    print("Redoing...")

def undoAction():
    print("Undoing...")

def documentation():
    print("Getting documentation...")

def kjv():
    print("Getting King James Version...")

def kjvs():
    print("Getting King James Version with Strong's...")

def sept():
    print("Getting Septuagint...")

def berean():
    print("Getting Berean...")

def scriptIndex():
    print("Getting Scripture Index...")


#-----------------------------------------------------------------------
# TOOLBAR FUNCTIONS
#-----------------------------------------------------------------------


def outText():
    print("out Text...")


#-----------------------------------------------------------------------
#HANDLE MOUSE EVENTS (FUNCTIONS)
#-----------------------------------------------------------------------

def leftClick(event):
    print("Left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

#-----------------------------------------------------------------------