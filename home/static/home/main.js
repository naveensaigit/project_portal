$(document).ready(function () {
    $(".searchable-select").select2();
    applyFilters();
});

$(document).on('click', '.task', function () {
    var project_id = $(this).attr('project_id');
    var page_number = $(this).attr('page_number');
    var task = $(this).attr('task');
    $.ajaxSetup({
        cache: false
    });
    $.ajax({
        type: "GET",
        url: `/project/task/?project_id=${project_id}&task=${task}&page_number=${page_number}`,
        success: function (response) {
            $("#projectNumber" + project_id).load(location.href + " #projectNumber" + project_id + " >.blog-container");
            console.log(task);
            if (task === "Star" || task === "Unstar") {
                $("#starred_projects").load(location.href + " #starred_projects" + ">#project-container")
            }
        },
        error: function (rs, e) {
            console.log(rs.responseText);
        },
    });
});

function applyFilters() {
    var url = new URL(window.location.href);
    if (url.searchParams.get("Status") != "")
        selectOption("id_Status", "Status");
    if (url.searchParams.get("Difficulty") != "")
        selectOption("id_Difficulty", "Difficulty");
    if (url.searchParams.get("FloatedBy") != "")
        selectOption("id_FloatedBy", "FloatedBy");
    if (url.searchParams.get("Duration") != "")
        selectOption("id_Duration", "Duration");
    if (url.searchParams.get("Tags") != "")
        selectTags();
}

function selectTags() {
    var params = window.location.href.split("&");
    var tag_ids = [];
    for (var i = 0; i < params.length; i++) {
        var param = params[i];
        if (param.includes('=')) {
            param = param.split('=');
            if (param[0] == "Tags") {
                tag_ids.push(param[1]);
            }
        }
    }
    var field = document.getElementById("id_Tags");
    for (let i = 0; i < field.children.length; i++) {
        var fieldOption = field.children[i];
        if (tag_ids.includes(fieldOption.value)) {
            var selected = document.createAttribute("selected");
            fieldOption.setAttributeNode(selected);
        }
    }

    var ulElement = document.getElementsByClassName('select2-selection__rendered')[1];

    for (var i = 0; i < tag_ids.length; i++) {
        var tag_id = tag_ids[i];
        var index = tags.findIndex(obj => obj.pk == tag_id);
        var tagName = tags[index].fields.Title;

        var liElement = document.createElement("li");
        liElement.setAttribute("class", "select2-selection__choice");
        liElement.setAttribute("title", tagName);

        var cutElement = document.createElement("span");
        cutElement.setAttribute("class", "select2-selection__choice__remove");
        cutElement.setAttribute("role", "presentation");
        cutElement.innerHTML = "x";
        liElement.appendChild(cutElement);

        var liContent = document.createTextNode(tagName);
        liElement.appendChild(liContent);

        var lastLiElement = ulElement.lastElementChild
        ulElement.insertBefore(liElement, lastLiElement);
    }
}

function selectOption(id, fieldName) {
    var url = new URL(window.location.href);
    var field = document.getElementById(id);
    var filterValue = url.searchParams.get(fieldName);

    if (fieldName == "Duration") {
        field.setAttribute('value', filterValue);
        return;
    }
    else if (fieldName == "FloatedBy") {
        var index = users.findIndex(obj => obj.pk == filterValue);
        filterValue = users[index].fields.username;

        var floatedByField = document.getElementById("select2-id_FloatedBy-container");
        floatedByField.setAttribute('title', filterValue);
        floatedByField.innerHTML = filterValue;
    }

    for (let i = 0; i < field.children.length; i++) {
        var fieldOption = field.children[i];
        if (fieldOption.innerHTML == filterValue) {
            var selected = document.createAttribute("selected");
            fieldOption.setAttributeNode(selected);
        }
    }
}