from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from graduates.models import Graduate, Speciality


def graduates(request, page_number=1, speciality="all"):
    filtered_graduates = Graduate.objects.all()
    current_page = Paginator(filtered_graduates, 9)

    return render_to_response('graduates.html', {'graduates': current_page.page(page_number),
                                                })


# Запрос из ajax, поле слева, поиск по фамилии
# Ответ отрисовываем в ajax_search.html
@csrf_exempt
def search_surname(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        search_text[0:0].upper()
    else:
        search_text=''
    print(search_text)
    graduates = Graduate.objects.filter(graduate_surname__startswith=search_text)[:10]
    return render_to_response('ajax_search.html', {'graduates': graduates,
                                                   })

#
@csrf_exempt
def search_faculty(request):
    search_val = request.POST['faculty_code']
    show_count_param = request.POST['show_count']
    graduates = Graduate.objects.filter(graduate_speciality__speciality_kaf__kaf_faculty__faculty_code=search_val)
    specialities = Speciality.objects.filter(speciality_kaf__kaf_faculty__faculty_code=search_val)
    show_count = int(show_count_param)

    return render_to_response('faculty_search.html', {'graduates': graduates[:show_count],
                                                      'specs': specialities,
    })

@csrf_exempt
def search_speciality(request):
    fac_val = request.POST['fac_name']
    show_count_param  = request.POST['show_count']
    show_count = int(show_count_param)
    search_val = request.POST['speciality_name']
    print(show_count)
    graduates = Graduate.objects.filter(graduate_speciality__speciality_name=search_val)
    specialities = Speciality.objects.filter(speciality_kaf__kaf_faculty__faculty_code=fac_val)

    return render_to_response('faculty_search.html', {'graduates': graduates[:show_count],
                                                        'specs': specialities,
                                                        'selected': 'selected="selected"',
                                                        'last_selected': search_val,
                                                        })


def get_graduate_description(request, id):
    print(id)
    graduate = Graduate.objects.get(id=id)

    return render_to_response('graduate.html', {'graduate': graduate,
                                                })

