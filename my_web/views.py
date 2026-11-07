from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def auth_page(request):
    return render(request, 'auth.html')


def courses_page(request):
    return render(request, 'courses.html')


def course_detail_page(request):
    return render(request, 'course_detail.html')


def profile_page(request):
    context = {
        'Username': 'Mahmud',
        'due_date': 'Today',
        'birth': 20100731,
        'Courses': 'Django',
        'Center_name': 'Soft Club'
    }
    return render(request, 'profile.html', context)