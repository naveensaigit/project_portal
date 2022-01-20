let mentor, tag, att, target, inputValue;
$(document).ready(function () {
    mentor = document.getElementById("id_Mentors");
    att = document.createAttribute("multiple");
    att.value = "multiple";
    mentor.setAttributeNode(att);

    $("#id_Mentors").select2({
        allowClear: 'true'
    });

    tag = document.getElementById("id_Tags");
    att = document.createAttribute("multiple");
    att.value = "multiple";
    tag.setAttributeNode(att);

    $("#id_Tags").select2({
        tags: true,
        tokenSeparators: [','],
    });
});

$('#id_Tags').on('select2:select', function (e) {
    var data = e.params.data;
    console.log(data);
    $.ajax({
        type:"GET",
        url:`/tag/new/?newTagTitle=${data.text}`,
        success: function (response) {
            console.log("GM");
            $("#div_id_Tags > div").load(location.href + " #id_Tags", function (responseTxt, statusTxt, xhr) {
                console.log(statusTxt);
                if (statusTxt == "success"){
                    $('#id_Tags').select2({
                        tags: true,
                        tokenSeparators: [','],
                    });
                }
                console.log(document.getElementById("id_Tags"));
                if (statusTxt == "error")
                    alert("Error: " + xhr.status + ": " + xhr.statusText);
            });
        }
    })
});

// function createNewTag() {
//     var newTagTitle = inputValue;
    // $.ajaxSetup({
    //     cache: false
    // });
    // $.ajax({
    //     type: "GET",
    //     url: `/tag/new/?newTagTitle=${newTagTitle}`,
    //     success: function (response) {
    //         $("#page-top > span").remove();
    //         $("#div_id_Tags > div").load(location.href + " #id_Tags", function (responseTxt, statusTxt, xhr) {
    //             if (statusTxt == "success") {
    //                 $("#id_Tags").select2({
    //                     "allowClear": 'true',
    //                     "language": {
    //                         "noResults": function () {
    //                             return "No Results Found <br> <a class='newTag'>Create New Tag</a>";
    //                         }
    //                     },
    //                     escapeMarkup: function (markup) {
    //                         return markup;
    //                     }
    //                 });
    //             }
    //             if (statusTxt == "error")
    //                 alert("Error: " + xhr.status + ": " + xhr.statusText);
    //             });
    //         },
    //         error: function (rs, e) {
    //         console.log(rs.responseText);
    //     },
    // });
// }