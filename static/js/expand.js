/**
 * Скрипт, отвечающий за расширение таблицы
 * При выборе группы сбрасывается специальность и наоборот
 */
$(function () {
    $('#expand').on('click', function () {
        show_count+=default_show_count;
        var spec = document.getElementById("filter_speciality").value;
        var group = document.getElementById("filter_group").value;
        if(spec != "none") {
            $.ajax({
                type: "POST",
                url: "/search_speciality/",
                data: {
                    'speciality_name': $('#filter_speciality').val(),
                    'fac_name': $('#filter_faculty').val(),
                    'show_count': show_count
                },
                success: searchFacultySuccess,
                dataType: 'html'
            });
            return;
        }
        if(group != "none") {
            $.ajax({
                type: "POST",
                url : "/search_by_group/",
                data: {
                    'group_number' : $('#filter_group').val(),
                    'show_count': show_count
                },
                success: searchFacultySuccess,
                dataType: 'html'
            });
            return;
        } else {
        $.ajax({
                type: "POST",
                url : "/search_faculty/",
                data: {
                    'faculty_code' : $('#filter_faculty').val(),
                    'show_count': show_count
                },
                success: searchFacultySuccess,
                dataType: 'html'
            });
        }
    })
});
