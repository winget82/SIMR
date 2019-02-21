/*FUNCTIONS TO RETURN THE VALUE OF SELECTION FROM SELECTIONS DROPDOWNS*/
/*------------------------------------------------------------------------------------------------*/
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
/*------------------------------------------------------------------------------------------------*/
/*FUNCTION TO RETURN A STRING OF COMPILED RETURNS FROM SELECTION DROPDOWNS TO BE USED
AS STRING TO SEARCH JSON FILES*/
/*------------------------------------------------------------------------------------------------*/
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
/*------------------------------------------------------------------------------------------------*/
/*upper right search box*/
/*------------------------------------------------------------------------------------------------*/
function searchBox() {
    var searchString = document.getElementById("sBoxForm").onsubmit = function() {
        document.getElementById("sBox").value;
        }        
    alert("function ran");    
    KJV(searchString);
    strKJV(searchString);
    //GETTING CROSS-ORIGIN REQUEST ERROR WITH THIS FUNCTION.  LOOK INTO HOW TO FIX.
    //https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
}
/*------------------------------------------------------------------------------------------------*/
/*JSON functions*/
/*------------------------------------------------------------------------------------------------*/
function KJV(searchString) {
    var kjv_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/KJV_json_d.json';
    var request_kjv = new XMLHttpRequest();
    request_kjv.open('GET', kjv_json);
    request_kjv.responseType = 'json';
    request_kjv.send();
    request_kjv.onload = function() {
        var KJVjsonResponse = request_kjv.response;
        populateKJVtext(KJVjsonResponse, searchString);
}

function populateKJVtext(KJVjsonResponse, searchString) {
    //console.log(KJVjsonResponse)
    var matchingResults = KJVjsonResponse[searchString];//https://stackoverflow.com/questions/922544/using-variable-keys-to-access-values-in-javascript-objects
    document.getElementById("kjvText").innerHTML = "<b>KJV:</b><br>" + "<i><b>" + searchString + "</b></i>" + ' - ' + matchingResults;
    //alert("function ran " + searchString);
    }
}
/*------------------------------------------------------------------------------------------------*/
function strKJV(searchString) {
    var strKJV_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/strKJVjson.json';
    var request_strKJV = new XMLHttpRequest();
    request_strKJV.open('GET', strKJV_json);
    request_strKJV.responseType = 'json';
    request_strKJV.send();
    request_strKJV.onload = function() {
        var strKJVjsonResponse = request_strKJV.response;
        populateStrKJVtext(strKJVjsonResponse, searchString);
}

function populateStrKJVtext(strKJVjsonResponse, searchString) {
    //console.log(strKJVjsonResponse)
    var matchingResults = strKJVjsonResponse[searchString];//https://stackoverflow.com/questions/922544/using-variable-keys-to-access-values-in-javascript-objects
    document.getElementById("strKJVText").innerHTML = "<b>KJV with Strong's Numbers:</b><br>" + "<i><b>" + searchString + "</b></i>" + ' - ' + matchingResults;
    //alert("function ran " + searchString);
    }
}
/*------------------------------------------------------------------------------------------------*/
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
/*------------------------------------------------------------------------------------------------*/
function Scriptindex(searchString) {
    var scriptindex_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/ScInd_json.json';
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
    //console.log(ScriptindexjsonResponse)
    var matchingResults = ScriptindexjsonResponse[searchString];//https://stackoverflow.com/questions/922544/using-variable-keys-to-access-values-in-javascript-objects  
    //need to format the following to display more aestheticly pleasing
    //may need to go back and reformat original scripture index data to be more easily manipulated
    //does not seem to be breaking cleanly
    //COULD TRY TO DO A ONETIME SPLIT ON REGEX MATCHES TO FNC, RHST, ADV, ETC WITH RETAINING THE REGEX MATCHES IN THE LIST
    var toPrintA = matchingResults.toString().split("\n");
    //remove empties in list
    var toPrintB = toPrintA.filter(Boolean);
    //build a string
    var toPrintC = "";
    for(var i = 0; i < toPrintB.length; i++){
        toPrintC += toPrintB[i];
    }
    //split back into list
    var toPrintD = toPrintC.split(",");
    //remove empties
    var toPrintE = toPrintD.filter(Boolean);
    //build a string
    var toPrintF = "";
    for(var i = 0; i < toPrintE.length; i++){
        toPrintF += toPrintE[i] + "<br>";
    }
    document.getElementById("scriptureindexText").innerHTML = "<b>TWI Scripture Index:</b><br>" + "<i><b>" + searchString + "</b></i>" + ':<br><br>' + toPrintF;
    //alert("function ran " + searchString);
}
/*------------------------------------------------------------------------------------------------*/
function searchClicked() {
    var searchString = searchChoice();
    KJV(searchString);
    strKJV(searchString);
    //Septuagin(searchString);
    //Berean(searchString);
    Scriptindex(searchString);
}
/*-------------------------------------------------------------------------------------------------*/
/*
function populateChapters() {
    var chapters_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/BiblesVerseCount.json';
    var request_chapters = new XMLHttpRequest();
    request_chapters.open('GET', chapters_json);
    request_chapters.responseType = 'json';
    request_chapters.send();
    request_chapters.onload = function() {
        var chapters_jsonResponse = request_chapters.response;
//need to set this up to get selected book and populate the chapters
//chapters_jsonResponse.Bible.KJV[1].Exodus.TotalChapters

}

function populateVerses() {
    var verses_json = 'https://raw.githubusercontent.com/winget82/SIMR/master/json_files/BiblesVerseCount.json';
    var request_verses = new XMLHttpRequest();
    request_verses.open('GET', verses_json);
    request_verses.responseType = 'json';
    request_verses.send();
    request_verses.onload = function() {
        var verses_jsonResponse = request_verses.response;
//need to set this up to get selected book and populate the chapters
//chapters_jsonResponse.Bible.KJV[1].Exodus.VersesEachCh[3] - will get total verse count for chapter 4

}
*/