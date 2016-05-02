/**
 * Created by qwe on 29.04.2016.
 */
$(function expand() {
    $('#expand').on('click', function () {
        show_count+=default_show_count;
        var spec = document.getElementById("filter_speciality")
        if(spec) {
            $.ajax({
                type: "POST",
                url: "/search_speciality/",
                data: {
                    'speciality_name' : $('#filter_speciality').val(),
                    'fac_name' : $('#filter_faculty').val(),
                    'show_count': show_count
                },
                success: searchFacultySuccess,
                dataType: 'html'
            });

        }else{
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
