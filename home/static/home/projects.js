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

colors = Array("#BEFFE0", "#FFD493", "#C9D8FF");

var tags = document.getElementById("tagsContainer").children;
for(var i = 1;i<tags.length;i++){
    var tag = tags[i];
    var ind = Math.floor(Math.random()*3);
    tag.style.backgroundColor = colors[ind];
}
$(".buttonContent").on("click",function(){
    unselect();
    var elem = $(this).context;
    if(elem.children[0].innerText == "Pre-requisite"){
        document.getElementById("proprereq").classList.remove("invisible");
    };
    if(elem.children[0].innerText == "Description"){
        document.getElementById("prodes").classList.remove("invisible");
    };
    if(elem.children[0].innerText == "Selection Criteria"){
        document.getElementById("proselcrit").classList.remove("invisible");
    };
    elem.className += " buttonSelected";
});
function unselect(){
    var buttons = document.getElementsByClassName('buttonContent');
    for(var i = 0;i<buttons.length;i++){
        var button = buttons[i];
        button.classList.remove("buttonSelected");
    }
    var buttonTriggers = document.getElementById('projectDescription').children;
    for(var i = 0;i<buttonTriggers.length;i++){
        var x = buttonTriggers[i];
        if(x.class != "invisible")
            x.classList.add("invisible");
    }
}
$(".viewAnswer").click(function () {
    var name = $(this).attr('userName');
    var projectID = $(this).attr('projectID');
    var acceptLink = "project/applyRequestTask/?project_id="+projectID+"&request_user="+name+"&task=Accept";
    var rejectLink = "project/applyRequestTask/?project_id="+projectID+"&request_user="+name+"&task=Reject";
    $('#rejectButton').attr("href",acceptLink);
    $('#acceptButton').attr("href",rejectLink);
    console.log(name);
    console.log(projectID);
});