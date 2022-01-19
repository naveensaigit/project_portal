// let mentor, tag, att, target, inputValue;
// $(document).ready(function () {
//     mentor = document.getElementById("id_Mentors");
//     att = document.createAttribute("multiple");
//     att.value = "multiple";
//     mentor.setAttributeNode(att);

//     $("#id_Mentors").select2({
//         allowClear: 'true'
//     });

//     tag = document.getElementById("id_Tags");
//     att = document.createAttribute("multiple");
//     att.value = "multiple";
//     tag.setAttributeNode(att);

//     $("#id_Tags").select2({
//         "allowClear": 'true',
//         "language": {
//             "noResults": function () {
//                 return "No Results Found <br> <a class='newTag'>Create New Tag</a>";
//             }
//         },
//         escapeMarkup: function (markup) {
//             return markup;
//         }
//     });

//     let targetSelector = "#div_id_Tags > div > span > span.selection > span > ul > li.select2-search.select2-search--inline > input";
//     target = document.querySelector(targetSelector);
//     target.addEventListener("keyup", function () {
//         inputValue = target.value;
//     });
// });

// $(document).on('click', '.newTag', function () {
//     var newTagTitle = inputValue;
//     $.ajaxSetup({
//         cache: false
//     });
//     $.ajax({
//         type: "GET",
//         url: `/tag/new/?newTagTitle=${newTagTitle}`,
//         success: function (response) {
//             $("#div_id_Tags > div").load(location.href + " #id_Tags", function (responseTxt, statusTxt, xhr) {
//                 if (statusTxt == "success") {
//                     $("#id_Tags").select2({
//                         "allowClear": 'true',
//                         "language": {
//                             "noResults": function () {
//                                 return "No Results Found <br> <a class='newTag'>Create New Tag</a>";
//                             }
//                         },
//                         escapeMarkup: function (markup) {
//                             return markup;
//                         }
//                     });
//                 }
//                 if (statusTxt == "error")
//                     alert("Error: " + xhr.status + ": " + xhr.statusText);
//                 });
//             },
//             error: function (rs, e) {
//             console.log(rs.responseText);
//         },
//     });
// });