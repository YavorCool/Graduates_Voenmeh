/**
 * Created by qwe on 16.04.2016.
 */

/* Поиск по фамилии, начинающейся с введенных букв */
$(function () {

    $('#search').keyup(function () {
        $.ajax({
            type: "POST",
            url : "/search/",
            data: {
                'search_text' : $('#search').val(),
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
$(function () {

    $('#filter_faculty').change(function () {
        $.ajax({
            type: "POST",
            url : "/search_faculty/",
            data: {
                'faculty_code' : $('#filter_faculty').val(),
            },
            success: searchFacultySuccess,
            dataType: 'html'
        });
    });
});


// Выбираем специальность и фильтруем по специальности, специальность - результат фильтрации по факультету
// Отрисовка в faculty_search.html
$(function () {

    $('#filter_speciality').change(function () {
        $.ajax({
            type: "POST",
            url : "/search_speciality/",
            data: {
                'speciality_name' : $('#filter_speciality').val(),
                'fac_name' : $('#filter_faculty').val(),
            },
            success: searchFacultySuccess,
            dataType: 'html'
        });
    });
});


function searchFacultySuccess(data, textStatus, jqXHR){
    $('#search_faculty_results').html(data);
}

