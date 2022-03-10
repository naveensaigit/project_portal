$(document).ready(function () {
    $(".searchable-select").select2();
    $(".searchable-select-clearable").select2({
        allowClear: 'true',
        placeholder: 'None',
    });
    applyFilters();
});

$(document).on('click', '.task', function () {
    var project_id = $(this).attr('project_id');
    var page_number = $(this).attr('page_number');
    var task = $(this).attr('task');
    $(this).attr("disabled", "true");
    if(task==="Star")
    {
        $(this).attr('task',"Unstar");
    }
    else if(task==="Unstar")
    {
        $(this).attr('task',"Star");
    }
    if(task==="Unlike")
    {
        var ele = parseInt($(this).children("div:first")[0].innerHTML);
        $(this).attr('task',"Like");
        $(this).children("div:first")[0].innerHTML=String(ele-1);
    }
    else if(task==="Like")
    {
        var ele = parseInt($(this).children("div:first")[0].innerHTML);
        $(this).attr('task',"Unlike");
        $(this).children("div:first")[0].innerHTML=String(ele+1);
    }
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
    $(this).attr("disabled", "false");
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

    var FilterBy = url.searchParams.get("FilterBy");
    if (FilterBy != null)
        $("#id_FilterBy").val(FilterBy);
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
