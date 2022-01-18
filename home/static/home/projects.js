let mentor, tag, att, target, value;
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
        "language": {
            "noResults": function () {
                return "No Results Found <br> <a href=tag/?value="+value+">Create New Tag</a>";
            }
        },
        escapeMarkup: function (markup) {
            return markup;
        }
    });

    let targetSelector = "#div_id_Tags > div > span > span.selection > span > ul > li.select2-search.select2-search--inline > input";
    target = document.querySelector(targetSelector);
    target.addEventListener("keyup", function(){
        value = target.value;
    });
});