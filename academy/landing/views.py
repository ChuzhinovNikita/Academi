from django.shortcuts import render
from .models import *
from .forms import LeadForm


# любой вид (функция) принемает первым атрибутом request
# а иначе запрос
# ибо интернет работает на принцепе requesr - response

def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses, 'teachers': teachers})


def greeting(request):
    teachers = Teacher.objects.all()
    return render(request, 'greeting.html', {'teachers': teachers})


def course(request, pk):
    # запрос на получение определённого обьекта
    course_data = Course.objects.get(pk=pk)
    form = LeadForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        # commit=False - приостановка сохранения данных идущих с формы в бд
        is_success = True
        instance.course = course_data
        instance.save()
        form = LeadForm()
    return render(request, 'course.html', {'course': course_data, 'form': form, 'is_success': is_success})


def check_leads(request):
    leads = Lead.objects.all()
    return render(
        request,
        'leads.html',
        {'leads': leads}
    )
