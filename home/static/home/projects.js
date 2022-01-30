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
                
                if (response.status == "ok") {
                    var newOption = new Option(response.tag_title, response.tag_id, false, false);
                    $('#id_Tags').append(newOption);
                    data.pop();
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

$('#id_OpenedFor_0').on('click', function(){
    var pre = "id_OpenedFor_";
    var mid = ['1_','2_','3_','4_'];
    var end = ['0','1','2','3'];
    if(this.checked){
        for(var i = 0;i<mid.length;i++){
            for(var j = 0;j<end.length;j++){
                var div = document.getElementById(pre+mid[i]+end[j]);
                div.checked = true;
            }
        }
    }
    else{
        for(var i = 0;i<mid.length;i++){
            for(var j = 0;j<end.length;j++){
                var div = document.getElementById(pre+mid[i]+end[j]);
                div.checked = false;
            }
        }
    }
});