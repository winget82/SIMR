/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myDropdownBook() {
    document.getElementById("myDropdownBook").classList.toggle("show");
}

function myDropdownChapter() {
    document.getElementById("myDropdownChapter").classList.toggle("show");
}

function myDropdownVerse() {
    document.getElementById("myDropdownVerse").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');}
        }
    }
}

//PROBLEMS WITH THESE FUNCTIONS THEY ALL CHANGE THE SAME BUTTON REGARDLESS OF DIFFERENT VARIABLE AND ID NAMES

function button_clickBook() {
    var buttons = document.getElementsByTagName("a");
    var buttonsCount = buttons.length;
    var textReturnedBook;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedBook = this.innerText;
            document.getElementById("book").innerHTML = textReturnedBook;
        };
    }
}

function button_clickChapter() {
    var buttons = document.getElementsByTagName("a");
    var buttonsCount = buttons.length;
    var textReturnedChapter;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedChapter = this.innerText;
            document.getElementById("chapter").innerHTML = textReturnedChapter;
        };
    }
}

function button_clickVerse() {
    var buttons = document.getElementsByTagName("a");
    var buttonsCount = buttons.length;
    var textReturnedVerse;
    for (var i = 0; i < buttonsCount; i += 1) {
        buttons[i].onclick = function(e) {
            //alert(this.innerText);
            textReturnedVerse = this.innerText;
            document.getElementById("verse").innerHTML = textReturnedVerse;
        };
    }
}