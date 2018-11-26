/*FUNCTIONS TO RETURN THE VALUE OF SELECTION FROM SELECTIONS DROPDOWNS*/
function selectedChoiceBook() {
    var buttons = document.getElementsByTagName("option");
    var buttonsCount = buttons.length;
    var textReturnedBook;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            alert(this.innerText);
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
            alert(this.innerText);
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
            alert(this.innerText);
            textReturnedVerse = this.innerText;
            return textReturnedVerse;
            //return this.value;
        };
    }
}

var Book = selectedChoiceBook();
var Chapter = selectedChoiceChapter();
var Verse = selectedChoiceVerse();

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
    alert(searchString);
    return searchString;
}