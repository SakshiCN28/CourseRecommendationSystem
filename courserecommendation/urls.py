from django.contrib import admin
from django.urls import path
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from courses.models import Course


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'courses/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not email or not password:
            messages.error(request, 'Please fill in all required fields.')

        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')

        elif User.objects.filter(username__iexact=username).exists():
            messages.error(request, 'This username is already taken.')

        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, 'This email is already registered.')

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                'Registration successful! Please log in.'
            )
            return redirect('login')

    return render(request, 'courses/register.html')


@login_required(login_url='login')
def home_view(request):
    courses = Course.objects.all()

    return render(request, 'courses/home.html', {
        'courses': courses
    })


@login_required(login_url='login')
def recommend_courses(request):
    recommended_courses = Course.objects.none()

    if request.method == 'POST':
        interest = request.POST.get('interest', '').strip()
        level = request.POST.get('level', '').strip()
        career_goal = request.POST.get('career_goal', '').strip()

        recommended_courses = Course.objects.all()

        if interest == 'Programming':
            recommended_courses = recommended_courses.filter(
                Q(category__icontains='Programming') |
                Q(course_name__icontains='Programming') |
                Q(skills__icontains='Programming') |
                Q(description__icontains='Programming')
            )

        elif interest == 'Web Development':
            recommended_courses = recommended_courses.filter(
                Q(category__icontains='Web Development') |
                Q(course_name__icontains='Web Development') |
                Q(skills__icontains='HTML') |
                Q(skills__icontains='CSS') |
                Q(skills__icontains='JavaScript') |
                Q(description__icontains='Web Development')
            )

        if level:
            recommended_courses = recommended_courses.filter(
                level__iexact=level
            )

        if career_goal:
            recommended_courses = recommended_courses.filter(
                career_field__icontains=career_goal
            )

    return render(request, 'courses/recommendations.html', {
        'recommended_courses': recommended_courses
    })


@login_required(login_url='login')
def search_courses(request):
    query = request.GET.get('q', '').strip()
    courses = Course.objects.all()

    if query:
        courses = courses.filter(
            Q(course_name__icontains=query) |
            Q(category__icontains=query) |
            Q(career_field__icontains=query) |
            Q(skills__icontains=query) |
            Q(description__icontains=query) |
            Q(level__icontains=query)
        ).distinct()

    return render(request, 'courses/search.html', {
        'courses': courses,
        'query': query
    })


@login_required(login_url='login')
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(request, 'courses/course_detail.html', {
        'course': course
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have logged out successfully.')
        return redirect('login')

    return redirect('home')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('home/', home_view, name='home'),
    path('recommend/', recommend_courses, name='recommend_courses'),
    path('search/', search_courses, name='search_courses'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('logout/', logout_view, name='logout'),
]