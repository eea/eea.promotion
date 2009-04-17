$(document).ready(function() {
        load();
        $('input[name=category]').change(function() {
            save();
        });
});


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
