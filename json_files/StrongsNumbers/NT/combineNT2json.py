import json

#IMPORT THE JSON FILES FOR EACH NT BOOK OF THE BIBLE

folderpath = 'P:/python_work/nates/SIMR/json_files/StrongsNumbers/NT/'

fn1 = '1Corinthians_json.json'
with open(folderpath + fn1) as f_obj_1:
	x1 = json.load(f_obj_1)

fn2 = '1John_json.json'
with open(folderpath + fn2) as f_obj_2:
	x2 = json.load(f_obj_2)

fn3 = '1Peter_json.json'
with open(folderpath + fn3) as f_obj_3:
	x3 = json.load(f_obj_3)

fn4 = '1Thessalonians_json.json'
with open(folderpath + fn4) as f_obj_4:
	x4 = json.load(f_obj_4)

fn5 = '1Timothy_json.json'
with open(folderpath + fn5) as f_obj_5:
	x5 = json.load(f_obj_5)

fn6 = '2Corinthians_json.json'
with open(folderpath + fn6) as f_obj_6:
	x6 = json.load(f_obj_6)

fn7 = '2John_json.json'
with open(folderpath + fn7) as f_obj_7:
	x7 = json.load(f_obj_7)

fn8 = '2Peter_json.json'
with open(folderpath + fn8) as f_obj_8:
	x8 = json.load(f_obj_8)

fn9 = '2Thessalonians_json.json'
with open(folderpath + fn9) as f_obj_9:
	x9 = json.load(f_obj_9)

fn10 = '2Timothy_json.json'
with open(folderpath + fn10) as f_obj_10:
	x10 = json.load(f_obj_10)

fn11 = '3John_json.json'
with open(folderpath + fn11) as f_obj_11:
	x11 = json.load(f_obj_11)

fn12 = 'Acts_json.json'
with open(folderpath + fn12) as f_obj_12:
	x12 = json.load(f_obj_12)

fn13 = 'Colossians_json.json'
with open(folderpath + fn13) as f_obj_13:
	x13 = json.load(f_obj_13)

fn14 = 'Ephesians_json.json'
with open(folderpath + fn14) as f_obj_14:
	x14 = json.load(f_obj_14)

fn15 = 'Galatians_json.json'
with open(folderpath + fn15) as f_obj_15:
	x15 = json.load(f_obj_15)

fn16 = 'Hebrews_json.json'
with open(folderpath + fn16) as f_obj_16:
	x16 = json.load(f_obj_16)

fn17 = 'James_json.json'
with open(folderpath + fn17) as f_obj_17:
	x17 = json.load(f_obj_17)

fn18 = 'John_json.json'
with open(folderpath + fn18) as f_obj_18:
	x18 = json.load(f_obj_18)

fn19 = 'Jude_json.json'
with open(folderpath + fn19) as f_obj_19:
	x19 = json.load(f_obj_19)

fn20 = 'Luke_json.json'
with open(folderpath + fn20) as f_obj_20:
	x20 = json.load(f_obj_20)

fn21 = 'Mark_json.json'
with open(folderpath + fn21) as f_obj_21:
	x21 = json.load(f_obj_21)

fn22 = 'Matthew_json.json'
with open(folderpath + fn22) as f_obj_22:
	x22 = json.load(f_obj_22)

fn23 = 'Philemon_json.json'
with open(folderpath + fn23) as f_obj_23:
	x23 = json.load(f_obj_23)

fn24 = 'Philippians_json.json'
with open(folderpath + fn24) as f_obj_24:
	x24 = json.load(f_obj_24)

fn25 = 'Revelation_json.json'
with open(folderpath + fn25) as f_obj_25:
	x25 = json.load(f_obj_25)

fn26 = 'Romans_json.json'
with open(folderpath + fn26) as f_obj_26:
	x26 = json.load(f_obj_26)

fn27 = 'Titus_json.json'
with open(folderpath + fn27) as f_obj_27:
	x27 = json.load(f_obj_27)

new = [x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+x22+x23+x24+x25+x26+x27]
all_NT_books = [j for p in new for j in p]

print(all_NT_books)

#WRITE TO JSON FILE
NTfilename = 'NT_json.json'
with open(NTfilename, 'w') as f_objNT:
	json.dump(all_NT_books, f_objNT)
