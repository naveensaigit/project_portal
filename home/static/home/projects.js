$(document).ready(function () {
    $("#id_Mentors").select2({
        multiple: true,
        allowClear: true
    });

    $("#id_Tags").select2({
        multiple: true,
        allowClear: true,
        tags: true,
        tokenSeparators: [','],
    }).on('select2:select', function (e) {
        var newTagTitle = e.params.data.text;
        var data = e.params.data;
        var select2Element = $(this);
        $.ajax({
            type:"GET",
            url:`/tag/new/?newTagTitle=${newTagTitle}`,
            success: function (response) {
                var newOption = new Option(data.text, data.id, false, false);
                console.log(newOption);
                $('#id_Tags').append(newOption);

            //     $("#div_id_Tags > div").load(location.href + " #id_Tags", function (responseTxt, statusTxt, xhr) {
            //         if (statusTxt == "success"){
            //             $('#id_Tags').select2({
            //                 tags: true,
            //                 tokenSeparators: [','],
            //             });
            //             // $('#id_Tags').val(tag_ids);
            //             // $('#id_Tags').trigger('change');
            //         }
            //         if (statusTxt == "error")
            //         alert("Error: " + xhr.status + ": " + xhr.statusText);
            //     });
            }
        })
    });
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