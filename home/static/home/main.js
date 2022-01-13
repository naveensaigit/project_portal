$(document).ready(function () {
    $(".searchable-select").select2();

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
        },
        error: function (rs, e) {
            console.log(rs.responseText);
        },
    });
});