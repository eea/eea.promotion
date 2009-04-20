$(document).ready(function() {
        load();
        disable();
        $('input[name=category]').change(function() {
            save();
            disable();
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


// Disable columns that aren't marked as active.
function disable() {
    $('input[name=category]').each(function() {
        var inputs = Array();
        switch ($(this).attr('value')) {
            case 'Front Page':
            inputs.push($('#form\\.frontpage_section'));
            break;
            case 'Themes':
            inputs.push($('#form\\.themepage_section'));
            inputs.push($('#form\\.themes'));
            break;
        }
        var disabled = $(this).attr('checked') == false;
        for (i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            input.attr('disabled', disabled);
            if (disabled) {
                input.addClass('disabled');
            } else if (input.hasClass('disabled')) {
                input.removeClass('disabled');
            }
        }
    });
}
