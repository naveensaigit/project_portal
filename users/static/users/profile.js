const selected = "#c9d8ff";
const unselected = "#f7f4f4";

$(document).ready(function () {
    var div = document.getElementById("projects0");
    var divbutton = document.getElementById("projects0button");
    divbutton.style.background = selected;
    div.removeAttribute("style");
});

var divs = ["projects0", "projects1", "projects2", "projects3"];
var visibleDivId = null;
function toggleVisibility(divId) {
    if (visibleDivId != divId) {
        visibleDivId = divId;
    }
    hideNonVisibleDivs();
}
function hideNonVisibleDivs() {
    var i, divId, div;
    for (i = 0; i < divs.length; i++) {
        divId = divs[i];
        div = document.getElementById(divId);
        divbutton = document.getElementById(divId + 'button');
        if (visibleDivId === divId) {
            div.style.display = "block";
            divbutton.style.background = selected;
        } else {
            div.style.display = "none";
            divbutton.style.background = unselected;
        }
    }
}

