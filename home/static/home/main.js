$(document).ready(function () {
    $(".searchable-select").select2();
    applyFilters();
});
$(document).on('click', '.task', function() {
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
            if(task === "Star" || task === "Unstar")
            {
                $("#starred_projects").load(location.href+" #starred_projects"+">#project-container")
            }
        },
        error: function (rs, e) {
            console.log(rs.responseText);
        },
    });
});

function applyFilters(){
    var url = new URL(window.location.href);

    selectOption("id_Status", "Status");
    selectOption("id_Difficulty", "Difficulty");
    selectOption("id_FloatedBy", "FloatedBy");
    selectOption("id_Duration", "Duration");
}

function selectOption(id, fieldName){
    var url = new URL(window.location.href);
    var field = document.getElementById(id);
    var filterValue = url.searchParams.get(fieldName);
    
    if(fieldName == "Duration"){
        field.setAttribute('value', filterValue);
        return;
    }
    else if(fieldName == "FloatedBy"){
        var index = users.findIndex(obj => obj.pk == filterValue);
        filterValue = users[index].fields.username;
    
        var floatedByField = document.getElementById("select2-id_FloatedBy-container");
        floatedByField.setAttribute('title', filterValue);
        floatedByField.innerHTML = filterValue;
    }

    for(let i = 0;i<field.children.length;i++){
        var fieldOption = field.children[i];
        if(fieldOption.innerHTML == filterValue){
            var selected = document.createAttribute("selected");
            fieldOption.setAttributeNode(selected);
        }
    }
}