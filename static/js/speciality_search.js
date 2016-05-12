/**
 * Created by qwe on 29.04.2016.
 */
// Выбираем специальность и фильтруем по специальности, специальность - результат фильтрации по факультету
// Отрисовка в faculty_search.html
$(function () {
    $('#filter_speciality').change(function () {
        show_count = default_show_count;
        document.getElementById("filter_group").value = "none";
        $.ajax({
            type: "POST",
            url : "/search_speciality/",
            data: {
                'speciality_name' : $('#filter_speciality').val(),
                'show_count': default_show_count,
            },
            success: searchFacultySuccess,
            dataType: 'html'
        });

        $.ajax({
            type: "POST",
            url : "/group_list_by_spec/",
            data: {
                'spec_name' : $('#filter_speciality').val(),
                'fac_val': $('#filter_faculty').val(),
            },
            success: groupListBySpec,
            dataType: 'html'
        });
    });
});

function searchFacultySuccess(data, textStatus, jqXHR){
    $('#search_faculty_results').html(data);
}

function groupListBySpec(data, textStatus, jqXHR){
    $('#filter_group').html(data);
}
