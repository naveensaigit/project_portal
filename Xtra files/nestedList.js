// Execute this after the site is loaded.
// $(function() {
//     // Find list items representing folders and
//     // style them accordingly.  Also, turn them
//     // into links that can expand/collapse the
//     // tree leaf.
//     $('li > ul').each(function(i) {
//         // Find this list's parent list item.
//         var parentLi = $(this).parent('li');

//         // Temporarily remove the list from the
//         // parent list item, wrap the remaining
//         // text in an anchor, then reattach it.
//         var subUl = $(this).remove();
//         parentLi.wrapInner('<a/>').find('a').click(function() {
//             // Make the anchor toggle the leaf display.
//             subUl.toggle();
//         });
//         parentLi.append(subUl);
//     });

//     // Hide all lists except the outermost.
//     $('ul ul').hide();
// });

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