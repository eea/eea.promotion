$(document).ready(function() {
        loc = $("#form\\.location");
        loc.click(function() {
            alert("ALTERED");
            filterInputFields(loc);
        });
        filterInputFields(loc);
});

// Only show inputs related to the chosen site location.
function filterInputFields(loc) {
    $("#form\\.theme_label").hide();
    $("#form\\.theme").hide();
    $("#form\\.frontpage_section").hide();
    $("#form\\.themepage_section").hide();
    $("#form\\.themepage_section_label").hide();
    $("#form\\.frontpage_section_label").hide();
    if (loc.attr("value") == "Front Page") {
        $("#form\\.frontpage_section_label").show();
        $("#form\\.frontpage_section").show();
    } else if (loc.attr("value") == "Themes") {
        $("#form\\.theme_label").show();
        $("#form\\.theme").show();
        $("#form\\.themepage_section_label").show();
        $("#form\\.themepage_section").show();
    }
}

