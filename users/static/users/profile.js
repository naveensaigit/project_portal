const selected = "#c9d8ff";
const unselected = "#f7f4f4";
var visibleDivId = 'projects0';

$(document).ready(function () {
    var elem = document.getElementById("projects0");
    elem.classList.remove("invisible");
    makeChanges();
});

function toggleVisibility(divId) {
    if (visibleDivId != divId) {
        var toHideElem = document.getElementById(visibleDivId);
        var toHideElemButton = document.getElementById(visibleDivId + "button");
        toHideElemButton.classList.remove('buttonSelected')
        toHideElem.classList.add('invisible');

        var toShowElem = document.getElementById(divId);
        var toShowElemButton = document.getElementById(divId + "button");
        toShowElemButton.classList.add('buttonSelected')
        toShowElem.classList.remove('invisible');

        visibleDivId = divId;
    }
}

function changeSize(x, size2, size1) {
    // size1 750
    // size2 1500

    // m = (size2 - size1)/750
    // c = size2 - m*1500

    // size = m*w + c 
    var w, m, c;
    w = window.innerWidth;
    m = (size2 - size1) / 650;
    c = size2 - m * 1500;
    x = String(m * w + c) + "px";
}

function makeChanges() {
    var elem = document.getElementsByClassName('projectButtonTitle');
    for (var i = 0; i < elem.length; i++) {
        changeSize(elem[i].style.fontSize, 15, 10);
    }

    elem = document.getElementsByClassName('projectsNumbers');
    for (var i = 0; i < elem.length; i++) {
        changeSize(elem[i].style.fontSize, 20, 15);
    }
}
window.onresize = makeChanges;