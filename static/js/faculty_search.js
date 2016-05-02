/**
 * Created by qwe on 16.04.2016.
 */
/* Поиск по фамилии, начинающейся с введенных букв */
var default_show_count = 2;
var show_count = default_show_count;

$(function () {
    $('#search').keyup(function () {
        $.ajax({
            type: "POST",
            url : "/search/",
            data: {
                'search_text' : $('#search').val(),
                'show_count' : default_show_count
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });

    $('#search').focusout(function(){
        $('#search_results').html('');
    });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#search_results').html(data);
}

//Выбираем факультет, фильтруем студентов по факультету, а также специальности, блок отрисовки в graduates.html
// Отрисовка в faculty_search.html

function filter_faculty(){

}


$(function () {

    $('#filter_faculty').change(function () {
        show_count = default_show_count;
        $.ajax({
            type: "POST",
            url : "/search_faculty/",
            data: {
                'faculty_code' : $('#filter_faculty').val(),
                'show_count': default_show_count,
            },
            success: searchFacultySuccess,
            dataType: 'html'
        });
    });
});

function searchFacultySuccess(data, textStatus, jqXHR){
    $('#search_faculty_results').html(data);
}

