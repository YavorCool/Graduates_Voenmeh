from django.core.paginator import Paginator
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from graduates.models import Graduate, Speciality, Faculty, Group, Kaf


def graduates(request):
    graduates = Graduate.objects.all()
    faculties = Faculty.objects.all()
    specs = Speciality.objects.all()
    groups = Group.objects.all()
    return render_to_response('graduates.html', {'graduates': graduates[:2],
                                                 'faculties': faculties,
                                                 'groups': groups,
                                                 'specs' : specs
                                                })


# Запрос из ajax, поле слева, поиск по фамилии
# Ответ отрисовываем в ajax_search.html
@csrf_exempt
def search_surname(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        search_text = search_text[0].upper() + search_text[1:]
    else:
        search_text=''
    show_count = request.POST['show_count']
    show_count = int(show_count)
    print(search_text)
    if(search_text == ''):
        graduates = []
        summary_count = 0
    else:
        graduates = Graduate.objects.filter(graduate_surname__startswith=search_text)
        summary_count = graduates.count()
    return render_to_response('ajax_search.html', {'graduates': graduates[:show_count],
                                                   'summary_count': summary_count
                                                   })


#
@csrf_exempt
def search_faculty(request):
    search_val = request.POST['faculty_code']
    show_count_param = request.POST['show_count']

    show_count = int(show_count_param)
    print(search_val)
    if search_val == "none":
        graduates = Graduate.objects.all()
    else:
        graduates = Graduate.objects.filter(graduate_faculty__faculty_code=search_val)

    return render_to_response('faculty_search.html', {'graduates': graduates[:show_count],
                                                     })

@csrf_exempt
def groups_by_faculty(request):
    search_val = request.POST['faculty_code']
    if search_val == "none":
        groups = Group.objects.all()
    else:
        groups = Group.objects.filter(group_faculty__faculty_code=search_val)

    return render_to_response('groups_list.html', {'groups': groups
                                                 })

@csrf_exempt
def specs_by_faculty(request):
    search_val = request.POST['faculty_code']
    if(search_val == "none"):
        specialities = Speciality.objects.all()
    else:
        specialities = Speciality.objects.filter(speciality_kaf__kaf_faculty__faculty_code=search_val)
    return render_to_response('specialities_list.html', {'specs': specialities
                                                 })


@csrf_exempt
def search_speciality(request):
    show_count_param = request.POST['show_count']
    show_count = int(show_count_param)
    search_val = request.POST['speciality_name']
    graduates = Graduate.objects.filter(graduate_group__group_speciality__speciality_name=search_val)

    return render_to_response('faculty_search.html', {'graduates': graduates[:show_count],
                                                      })


@csrf_exempt
def filter_by_group(request):
    search_val = request.POST['group_number']
    show_count = request.POST['show_count']
    show_count = int(show_count)
    graduates = Graduate.objects.filter(graduate_group__group_number=search_val)

    return render_to_response('faculty_search.html', {'graduates': graduates[:show_count],
                                                      })



@csrf_exempt
def spec_list_by_group(request):
    group_number = request.POST["group_number"];
    group = Group.objects.get(group_number=group_number)
    selected_spec = group.group_speciality
    faculty = group.group_faculty
    specs = Speciality.objects.filter(speciality_kaf__kaf_faculty=faculty)

    return render_to_response('specialities_list.html', {
        'selected_spec': selected_spec,
        'specs': specs,
    })


@csrf_exempt
def group_list_by_spec(request):
    spec_name = request.POST['spec_name']
    fac_val = request.POST['fac_val']
    if spec_name != "none":
        spec = Speciality.objects.get(speciality_name=spec_name)
        groups = spec.group_set.all()
    else:
        if fac_val != "none":
            groups = Group.objects.filter(group_faculty__faculty_code=fac_val)
        else:
            groups = Group.objects.all()

    return render_to_response('groups_list.html', {'groups': groups})


def get_graduate_description(request, id):
    graduate = Graduate.objects.get(id=id)

    return render_to_response('graduate.html', {'graduate': graduate,
                                                })


def get_faculty_description(request, id):
    faculty = Faculty.objects.get(id=id)
    kafs = faculty.kaf_set.all()

    return render_to_response('faculty.html', {'faculty': faculty,
                                               'kafs': kafs
                                               })


def get_kaf_description(request, id):
    kaf = Kaf.objects.get(id=id)
    specs = kaf.speciality_set.all()

    return render_to_response('kaf.html', {'kaf': kaf,
                                               'specs': specs
                                               })

def get_spec_description(request, id):
    spec = Speciality.objects.get(id=id)

    return render_to_response('spec.html', {'spec': spec
                                               })

