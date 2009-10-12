$(document).ready(function() {
        load();
        updateView();
        $('input[name=category]').click(function() {
            updateView();
            save();
        });
});


// If a promotion is global, it should be placed on the frontpage in the
// spotlight section. Otherwise it wouldn't show there at all. Also themes
// should be deactivated to avoid duplicate promotions.
function updateView() {
    if ($('#global input[name=category]').attr('checked') == true) {
        var input = $('#form\\.frontpage_section');
        input.attr('value', 'spotlight');
        $('#frontpage input[name=category]').attr('checked', true);
        $('#themes input[name=category]').removeAttr('checked');
        $("#frontpage, #themes").hide('slow');
    } else {
        $("#frontpage, #themes").show('slow');
    }
}


// Parse hidden locations field and check corresponding checkboxes.
function load() {
    var input = $('input[name=form\\.locations]').attr('value');
    $('input[name=category]').each(function() {
        var name = $(this).attr('value');
        var checked = input.indexOf(name) >= 0;
        $(this).attr('checked', checked);
    });
}


// Update hidden locations field with enabled checkboxes.
function save() {
    var output_val = ''
    $('input[name=category]').each(function() {
        if ($(this).attr('checked') == true) {
            output_val += "'" + $(this).attr('value') + "', "
        }
    });
    // remove the trailing ', '
    output_val = output_val.slice(0, output_val.length - 2);
    $('input[name=form\\.locations]').attr('value', output_val);
}
