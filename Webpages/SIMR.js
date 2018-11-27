/*FUNCTIONS TO RETURN THE VALUE OF SELECTION FROM SELECTIONS DROPDOWNS*/
function selectedChoiceBook() {
    var buttons = document.getElementsByTagName("option");
    var buttonsCount = buttons.length;
    var textReturnedBook;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedBook = this.innerText;
            return textReturnedBook;
            //return this.value;
        };
    }
}

function selectedChoiceChapter() {
    var buttons = document.getElementsByTagName("option");
    var buttonsCount = buttons.length;
    var textReturnedChapter;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedChapter = this.innerText;
            return textReturnedChapter;
            //return this.value;
        };
    }
}

function selectedChoiceVerse() {
    var buttons = document.getElementsByTagName("option");
    var buttonsCount = buttons.length;
    var textReturnedVerse;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedVerse = this.innerText;
            return textReturnedVerse;
            //return this.value;
        };
    }
}

/*FUNCTION TO RETURN A STRING OF COMPILED RETURNS FROM SELECTION DROPDOWNS TO BE USED
AS STRING TO SEARCH JSON FILES*/
function searchChoice() {
    var book = document.getElementById("BookSelect");
    var i = book.selectedIndex;
    var Book = book.options[i].text;
    
    var chapter = document.getElementById("ChapterSelect");
    var i = chapter.selectedIndex;
    var Chapter = chapter.options[i].text;

    var verse = document.getElementById("VerseSelect");
    var i = verse.selectedIndex;
    var Verse = verse.options[i].text;
    
    var searchString = Book + " " + Chapter + Verse;
    //alert(searchString);
    return searchString;
}

/*JSON functions*/
/*see https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON*/
    
function KJV(searchString) {
    var kjv_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/KJV_json.json';
    var request_kjv = new XMLHttpRequest();
    request_kjv.open('GET', kjv_json);
    request_kjv.responseType = 'json';
    request_kjv.send();
    request_kjv.onload = function() {
        var KJVjsonResponse = request_kjv.response;
        populateKJVtext(KJVjsonResponse, searchString);
    }
}

function populateKJVtext(KJVjsonResponse, searchString) {
    //function to search through kjv json file and find match according to scripture searched for
    //changes text (HTML) to show results of search on webpage
    //found = next(i for i in scriptures_lst if verse in i)
    //return found
}

function Berean(searchString) {
    var berean_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/berean_json.json';
    var request_berean = new XMLHttpRequest();
    request_berean.open('GET', berean_json);
    request_berean.responseType = 'json';
    request_berean.send();
    request_berean.onload = function() {
        var BereanjsonResponse = request_berean.response;
        populateBereanText(BereanjsonResponse, searchString);
    }
}

function populateBereanText(BereanjsonResponse, searchString) {
    //function to search through berean json file and find match according to scripture searched for
    //changes text (HTML) to show results of search on webpage
    //if berean_inp in berean:
        //bi = berean.index(berean_inp)  # This is based on verse seached for.
        //# Sets bi to the index of verse searched for
        //return bi
}

function Scriptindex(searchString) {
    var scriptindex_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/scriptindex_json.json';
    var request_scriptindex = new XMLHttpRequest();
    request_scriptindex.open('GET', scriptindex_json);
    request_scriptindex.responseType = 'json';
    request_scriptindex.send();
    request_scriptindex.onload = function() {
        var ScriptindexjsonResponse = request_scriptindex.response;
        populateScriptindexText(ScriptindexjsonResponse, searchString);
    }
}

function populateScriptindexText(ScriptindexjsonResponse, searchString) {
    //function to search through scripture index json file and find match according to scripture searched for
    //changes text (HTML) to show results of search on webpage
    //found2 = next(i for i in twi_index if twi_inp in i)
    //return found2
}

function searchClicked() {
    var searchString = searchChoice();
    KJV(searchString);
    Berean(searchString);
    Scriptindex(searchString);
}