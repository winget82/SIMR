import json

#IMPORT THE JSON FILES FOR EACH NT BOOK OF THE BIBLE

folderpath = 'P:/python_work/nates/SIMR/json_files/StrongsNumbers/OT/'

fn1 = '1Chronicles_json.json'
with open(folderpath + fn1) as f_obj_1:
	x1 = json.load(f_obj_1)

fn2 = '1Kings_json.json'
with open(folderpath + fn2) as f_obj_2:
	x2 = json.load(f_obj_2)

fn3 = '1Samuel_json.json'
with open(folderpath + fn3) as f_obj_3:
	x3 = json.load(f_obj_3)

fn4 = '2Chronicles_json.json'
with open(folderpath + fn4) as f_obj_4:
	x4 = json.load(f_obj_4)

fn5 = '2Kings_json.json'
with open(folderpath + fn5) as f_obj_5:
	x5 = json.load(f_obj_5)

fn6 = '2Samuel_json.json'
with open(folderpath + fn6) as f_obj_6:
	x6 = json.load(f_obj_6)

fn7 = 'Amos_json.json'
with open(folderpath + fn7) as f_obj_7:
	x7 = json.load(f_obj_7)

fn8 = 'Daniel_json.json'
with open(folderpath + fn8) as f_obj_8:
	x8 = json.load(f_obj_8)

fn9 = 'Deuteronomy_json.json'
with open(folderpath + fn9) as f_obj_9:
	x9 = json.load(f_obj_9)

fn10 = 'Ecclesiastes_json.json'
with open(folderpath + fn10) as f_obj_10:
	x10 = json.load(f_obj_10)

fn11 = 'Esther_json.json'
with open(folderpath + fn11) as f_obj_11:
	x11 = json.load(f_obj_11)

fn12 = 'Exodus_json.json'
with open(folderpath + fn12) as f_obj_12:
	x12 = json.load(f_obj_12)

fn13 = 'Ezekiel_json.json'
with open(folderpath + fn13) as f_obj_13:
	x13 = json.load(f_obj_13)

fn14 = 'Ezra_json.json'
with open(folderpath + fn14) as f_obj_14:
	x14 = json.load(f_obj_14)

fn15 = 'Genesis_json.json'
with open(folderpath + fn15) as f_obj_15:
	x15 = json.load(f_obj_15)

fn16 = 'Habakkuk_json.json'
with open(folderpath + fn16) as f_obj_16:
	x16 = json.load(f_obj_16)

fn17 = 'Haggai_json.json'
with open(folderpath + fn17) as f_obj_17:
	x17 = json.load(f_obj_17)

fn18 = 'Hosea_json.json'
with open(folderpath + fn18) as f_obj_18:
	x18 = json.load(f_obj_18)

fn19 = 'Isaiah_json.json'
with open(folderpath + fn19) as f_obj_19:
	x19 = json.load(f_obj_19)

fn20 = 'Jeremiah_json.json'
with open(folderpath + fn20) as f_obj_20:
	x20 = json.load(f_obj_20)

fn21 = 'Job_json.json'
with open(folderpath + fn21) as f_obj_21:
	x21 = json.load(f_obj_21)

fn22 = 'Joel_json.json'
with open(folderpath + fn22) as f_obj_22:
	x22 = json.load(f_obj_22)

fn23 = 'Jonah_json.json'
with open(folderpath + fn23) as f_obj_23:
	x23 = json.load(f_obj_23)

fn24 = 'Joshua_json.json'
with open(folderpath + fn24) as f_obj_24:
	x24 = json.load(f_obj_24)

fn25 = 'Judges_json.json'
with open(folderpath + fn25) as f_obj_25:
	x25 = json.load(f_obj_25)

fn26 = 'Lamentations_json.json'
with open(folderpath + fn26) as f_obj_26:
	x26 = json.load(f_obj_26)

fn27 = 'Leviticus_json.json'
with open(folderpath + fn27) as f_obj_27:
	x27 = json.load(f_obj_27)

fn28 = 'Malachi_json.json'
with open(folderpath + fn28) as f_obj_28:
	x28 = json.load(f_obj_28)

fn29 = 'Micah_json.json'
with open(folderpath + fn29) as f_obj_29:
	x29 = json.load(f_obj_29)

fn30 = 'Nahum_json.json'
with open(folderpath + fn30) as f_obj_30:
	x30 = json.load(f_obj_30)

fn31 = 'Nehemiah_json.json'
with open(folderpath + fn31) as f_obj_31:
	x31 = json.load(f_obj_31)

fn32 = 'Numbers_json.json'
with open(folderpath + fn32) as f_obj_32:
	x32 = json.load(f_obj_32)

fn33 = 'Obadiah_json.json'
with open(folderpath + fn33) as f_obj_33:
	x33 = json.load(f_obj_33)

fn34 = 'Proverbs_json.json'
with open(folderpath + fn34) as f_obj_34:
	x34 = json.load(f_obj_34)

fn35 = 'Psalms_json.json'
with open(folderpath + fn35) as f_obj_35:
	x35 = json.load(f_obj_35)

fn36 = 'Ruth_json.json'
with open(folderpath + fn36) as f_obj_36:
	x36 = json.load(f_obj_36)

fn37 = 'SongofSolomon_json.json'
with open(folderpath + fn37) as f_obj_37:
	x37 = json.load(f_obj_37)

fn38 = 'Zechariah_json.json'
with open(folderpath + fn38) as f_obj_38:
	x38 = json.load(f_obj_38)

fn39 = 'Zephaniah_json.json'
with open(folderpath + fn39) as f_obj_39:
	x39 = json.load(f_obj_39)

newOT = [x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+x22+x23+x24+x25+x26+x27+x28+x29+x30+x31+x32+x33+x34+x35+x36+x37+x38+x39]
all_OT_books = [j for p in newOT for j in p]

print(all_OT_books)

#WRITE TO JSON FILE
OTfilename = 'OT_json.json'
with open(OTfilename, 'w') as f_objOT:
	json.dump(all_OT_books, f_objOT)
