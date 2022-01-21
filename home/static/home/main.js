$(document).ready(function () {
    $(".searchable-select").select2();
    $(".searchable-select-clearable").select2({
        allowClear: 'true'
    });
    applyFilters();
    addFilteredTags();
});


function addFilteredTags() {
    var div = document.querySelector('#content > div > div > div.blog-container > div');
    var tag_ids = $('#id_Tags').val();
    if (tag_ids == null) {
        var aElement = document.createElement("a");
        aElement.setAttribute("href", ``);
        aElement.innerHTML = "None";

        div.appendChild(aElement);
    }
    else {
        for (var i = 0; i < tag_ids.length; i++) {
            var tag_id = tag_ids[i];

            var Title = tags[tags.findIndex(obj => obj.pk == tag_id)].fields.Title;

            var aElement = document.createElement("a");
            aElement.setAttribute("href", `/?Tags=${tag_id}`);
            aElement.innerHTML = Title;

            div.appendChild(aElement);
        }
    }
}

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
            if (task === "Star" || task === "Unstar") {
                $("#starred_projects").load(location.href + " #starred_projects" + ">#project-container")
            }
        },
        error: function (rs, e) {
            console.log(rs.responseText);
        },
    });
});

function clearFilters() {
    var url = new URL(window.location.href);
    var newUrlString = window.location.href.split('?')[0];
    var page = url.searchParams.get("page");
    if (page != null) {
        newUrlString += `?page=${page}`;
    }
    window.location.href = new URL(newUrlString);
}

function applyFilters() {
    var url = new URL(window.location.href);

    var status = url.searchParams.get("Status");
    if (status != null && status != "")
        $("#id_Status").val(status);

    var difficulty = url.searchParams.get("Difficulty");
    if (difficulty != null && difficulty != "")
        $("#id_Difficulty").val(difficulty);

    var floatedBy = url.searchParams.get("FloatedBy");
    if (floatedBy != null && floatedBy != "") {
        $('#id_FloatedBy').val(floatedBy); // Select the option with a value of '1'
        $('#id_FloatedBy').trigger('change'); // Notify any JS components that the value changed
    }

    // var duration = url.searchParams.get("Duration");
    // if (duration != null && duration != "")
    //     selectOption("id_Duration", "Duration");

    var tags = url.searchParams.get("Tags");
    if (tags != null && tags != "")
        selectTags();
}

function selectTags() {
    var params = window.location.href.split("?");
    params = params[1].split("&");
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
    $('#id_Tags').val(tag_ids);
    $('#id_Tags').trigger('change');
}
