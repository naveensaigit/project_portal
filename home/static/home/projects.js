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

$('#id_OpenedFor_0').on('click', function () {
    var pre = "id_OpenedFor_";
    var mid = ['1_', '2_', '3_', '4_'];
    var end = ['0', '1', '2', '3'];
    if (this.checked) {
        for (var i = 0; i < mid.length; i++) {
            for (var j = 0; j < end.length; j++) {
                var div = document.getElementById(pre + mid[i] + end[j]);
                div.checked = true;
            }
        }
    }
    else {
        for (var i = 0; i < mid.length; i++) {
            for (var j = 0; j < end.length; j++) {
                var div = document.getElementById(pre + mid[i] + end[j]);
                div.checked = false;
            }
        }
    }
});

function toggleCheckBoxes(branchCode){
    var state = false;
    var branch = ['#id_OpenedFor_'+branchCode+'_0', '#id_OpenedFor_'+branchCode+'_1', '#id_OpenedFor_'+branchCode+'_2', '#id_OpenedFor_'+branchCode+'_3']
    for (var i = 0; i < branch.length; i++) {
        if ($(branch[i]).is(':checked')==false)
            state = true;
    }
    for (var i = 0; i < branch.length; i++) {
        $(branch[i]).prop('checked', state);
    }
}
$('#div_id_OpenedFor > div > strong:nth-child(2)').on('click', function () {
    toggleCheckBoxes('1');
});
$('#div_id_OpenedFor > div > strong:nth-child(7)').on('click', function () {
    toggleCheckBoxes('2');
});
$('#div_id_OpenedFor > div > strong:nth-child(12)').on('click', function () {
    toggleCheckBoxes('3');
});
$('#div_id_OpenedFor > div > strong:nth-child(17)').on('click', function () {
    toggleCheckBoxes('4');
});

$('.TreeInput').prop('checked', true);
function checkParents($li, state) {
    var $siblings = $li.siblings();
    var $parent = $li.parent().closest('li');
    state = state && $siblings.children('label').find('input').prop('checked');
    $parent.children('label').find('input').prop('checked', state);
    if ($parent.parents('li').length)
        checkParents($parent, state);
}

$('.TreeInput').change(function () {
    var $li = $(this).closest('li');
    var state = $(this).prop('checked');

    // check all children
    $li.find('.TreeInput').prop('checked', state);

    // check all parents, as applicable
    if ($li.parents('li').length)
        checkParents($li, state);
});