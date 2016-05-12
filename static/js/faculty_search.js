/**
 * Created by qwe on 16.04.2016.
 */
/* Поиск по фамилии, начинающейся с введенных букв */
var default_show_count = 2;//Начальное количество показываемых записей общей таблицы
var show_count = default_show_count;//Колиество показываемых записей
                                    //общей таблицы , увеличивается на default_show_count при расширении

var surname_search_show_count = 2;//Количество записей, показываемых в таблицы с поиском по фамилии

//Скрипт с поиском по фамилии
$(function () {
    $('#search').keyup(function () {
        $.ajax({
            type: "POST",
            url : "/search/",
            data: {
                'search_text' : $('#search').val(),
                'show_count' : surname_search_show_count
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
/*
    $('#search').focusout(function(){
        $('#search_results').html('');
    })*/
});

function searchSuccess(data, textStatus, jqXHR){
    $('#search_results').html(data);
}

//Выбираем факультет, фильтруем студентов по факультету, а также специальности, блок отрисовки в graduates.html
// Отрисовка в faculty_search.html

function filter_faculty(){

}

/*
*Скрипт, срабатывающий при выборе факультета
* Отображает выпускников данного факультета
* Выводит в select с группами и специальностями группы и специальности выбранного факультета
 */
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

        $.ajax({
            type: "POST",
            url : "/groups_by_faculty/",
            data: {
                'faculty_code' : $('#filter_faculty').val(),
            },
            success: searchGroupsByFacultySuccess,
            dataType: 'html'
        });
        
        $.ajax({
            type: "POST",
            url : "/specs_by_faculty/",
            data: {
                'faculty_code' : $('#filter_faculty').val(),
            },
            success: searchSpecsByFacultySuccess,
            dataType: 'html'
        });
    });
});

function searchFacultySuccess(data, textStatus, jqXHR){
    $('#search_faculty_results').html(data);
}

function searchGroupsByFacultySuccess(data, textStatus, jqXHR){
    $('#filter_group').html(data);
}

function searchSpecsByFacultySuccess(data, textStatus, jqXHR){
    $('#filter_speciality').html(data);
}


