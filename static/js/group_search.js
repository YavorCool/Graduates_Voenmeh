
// Выбираем группу и фильтруем по группе
// Отрисовка в faculty_search.html
$(function () {
    $('#filter_group').change(function () {
        show_count = default_show_count;
        document.getElementById("filter_speciality").value = "none";
        $.ajax({
            type: "POST",
            url : "/search_by_group/",
            data: {
                'group_number' : $('#filter_group').val(),
                'fac_name' : $('#filter_faculty').val(),
                'show_count': default_show_count,
            },
            success: searchFacultySuccess,
            dataType: 'html'
        });

        $.ajax({
            type: "POST",
            url : "/spec_list_by_group/",
            data: {
                'group_number' : $('#filter_group').val()
            },
            success: searchSpecListByGroupSuccess,
            dataType: 'html'
        });
    });
});

function searchFacultySuccess(data, textStatus, jqXHR){
    $('#search_faculty_results').html(data);
}

function searchSpecListByGroupSuccess(data, textStatus, jqXHR){
    $('#filter_speciality').html(data);
}
