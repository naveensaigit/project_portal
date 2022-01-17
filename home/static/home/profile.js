$(document).ready(function () {
    var div = document.getElementById("projects0");
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
        if (visibleDivId === divId) {
            div.style.display = "block";
        } else {
            div.style.display = "none";
        }
    }
}

