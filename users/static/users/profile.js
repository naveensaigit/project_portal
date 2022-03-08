const selected = "#c9d8ff";
const unselected = "#f7f4f4";
var visibleDivId = 'projects0';

$(document).ready(function () {
    var elem = document.getElementById("projects0");
    elem.classList.remove("invisible");
});

function toggleVisibility(divId) {
    if (visibleDivId != divId) {
        var toHideElem = document.getElementById(visibleDivId);
        var toHideElemButton = document.getElementById(visibleDivId+"button");
        toHideElemButton.classList.remove('buttonSelected')
        toHideElem.classList.add('invisible');

        var toShowElem = document.getElementById(divId);
        var toShowElemButton = document.getElementById(divId+"button");
        toShowElemButton.classList.add('buttonSelected')
        toShowElem.classList.remove('invisible');

        visibleDivId = divId;
    }
}

