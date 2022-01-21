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
        createTag: function (params) {
            var term = $.trim(params.term);
            if (term === '') {
                return null;
            }
            return {
                id: term,
                text: term.toUpperCase(),
                newTag: true // add additional parameters
            }
        },
        insertTag: function (data, tag) {
            // Insert the tag at the end of the results
            data.push(tag);
        },
        templateResult: function (data) {
            var $result = $("<span></span>");
            $result.text(data.text);
            if (data.newTag) {
                $result.append(" <em>(create new tag)</em>");
            }
            return $result;
        },

    }).on('select2:select', function (e) {
        var newTagTitle = e.params.data.text;
        $.ajax({
            type: "GET",
            url: `/tag/new/?newTagTitle=${newTagTitle}`,
            success: function (response) {
                data = $('#id_Tags').val();
                data.pop();

                if (response.status == "ok") {
                    var newOption = new Option(response.tag_title, response.tag_id, false, false);
                    $('#id_Tags').append(newOption);
                    data.push(newOption.value);
                }
                else if (response.status == "tag already exists") {
                    data.push(response.tag_id);
                }

                $('#id_Tags').val(null).trigger('change');
                $('#id_Tags').val(data).trigger('change');

            }
        })
    });
});