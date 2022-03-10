$(document).ready(function () {
    moveFilters();
});

function moveFilters() {
    var controls = document.getElementById("tableControls");
    var bootstrapControlsDiv = document.querySelector("#tableContainer > div.bootstrap-table.bootstrap4 > div.fixed-table-toolbar");
    controls.innerHTML = bootstrapControlsDiv.outerHTML;
    bootstrapControlsDiv.innerHTML = "";
}

colors = Array("#BEFFE0", "#FFD493", "#C9D8FF");
var tagsToDisplay = document.getElementById("tagsContainer").children;
for(var i = 1;i<tagsToDisplay.length;i++){
    var tag = tagsToDisplay[i];
    var ind = Math.floor(Math.random()*3);
    tag.style.backgroundColor = colors[ind];
}
function unselect(){
    var buttons = document.getElementsByClassName('buttonContent');
    for(var i = 0;i<buttons.length;i++){
        var button = buttons[i];
        button.classList.remove("buttonSelected");
    }
    var buttonTriggers = document.getElementById('projectDescription').children;
    for(var i = 0;i<buttonTriggers.length;i++){
        var x = buttonTriggers[i];
        if(x.class !== "invisible")
        x.classList.add("invisible");
    }
    console.log(buttonTriggers)
}
function takeAction(elem,action){
    unselect();
    if(action === "Pre-requisite"){
        document.getElementById("proprereq").classList.remove("invisible");
    };
    if(action === "Description"){
        document.getElementById("prodes").classList.remove("invisible");
    };
    if(action === "Selection Criteria"){
        document.getElementById("proselcrit").classList.remove("invisible");
    };
    elem.className += " buttonSelected";
}

$("#applyQuestion").on("input", function(){
    var input = document.querySelector('#applyQuestion');
    var projectId = $("#applyNow").attr("projectId");

    var link = `/project/task/?task=Apply&project_id=${projectId}&message=${input.value}`;
    $("#applyModal > div > div > div.modal-footer > a").attr("href", link);
});

$(".viewAnswer").click(function () {
    var user_profile_id = $(this).attr('user_profile_id');
    var application_id = $(this).attr('application_id');

    var user_profile = user_profiles[user_profiles.findIndex(obj => obj.pk == user_profile_id)].fields;
    var user = users[users.findIndex(obj => obj.pk == user_profile['user'])].fields;
    var application = applications[applications.findIndex(obj => obj.pk == application_id)].fields;

    var acceptLink = "applyRequestTask/?project_id="+application['Project']+"&request_user="+user['username']+"&task=Accept";
    var rejectLink = "applyRequestTask/?project_id="+application['Project']+"&request_user="+user['username']+"&task=Reject";
    
    var skills = "";
    for(var i = 0;i<user_profile['techskills'].length;i++)
        skills += tags[tags.findIndex(obj => obj.pk == user_profile['techskills'][i])].fields.Title + " ";

    $("#Profile_image").html("<img src = \"/media/" + user_profile['image']+"\"></img>");
    $("#Name").html(user['first_name']+" "+user['last_name']);
    $("#Year").html(user_profile['year']+" year-"+user_profile['branch']);
    $("#Rollno").html(user_profile['rollno']);
    $("#SkillsContent").html(skills);
    $("#Linkedin_link").html(user_profile['linked_in_link']);
    $("#Portfolio_link").html(user_profile['portfolio_link']);
    $("#Github_link").html(user_profile['github_link']);
    $("#Resume").html("<a href = \"/media/" + user_profile['cv']+"\" target = \"_blank\">Resume</a>");
    $("#Message").html(application['Message']);
    $('#rejectButton').attr("href",rejectLink);
    $('#acceptButton').attr("href",acceptLink);
});

var $table = $('#table');
$(function () {
    $('#toolbar').find('select').change(function () {
        var filter = { status: $(this).val() };
        if ($(this).val() == "") {
            filter = {};
        }
        console.log(filter);
        $table.bootstrapTable('filterBy', filter);
    });
});