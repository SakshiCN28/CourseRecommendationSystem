from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Course


def home(request):
    courses = Course.objects.all()

    return render(request, 'courses/home.html', {
        'courses': courses
    })


def recommend_courses(request):
    recommended_courses = Course.objects.none()

    if request.method == 'POST':
        interest = request.POST.get('interest', '')
        level = request.POST.get('level', '')
        career_goal = request.POST.get('career_goal', '')

        recommended_courses = Course.objects.all()

        if interest:
            recommended_courses = recommended_courses.filter(
                category__iexact=interest
            )

        if level:
            recommended_courses = recommended_courses.filter(
                level__iexact=level
            )

        if career_goal:
            recommended_courses = recommended_courses.filter(
                career_field__iexact=career_goal
            )

    return render(request, 'courses/recommendations.html', {
        'recommended_courses': recommended_courses
    })


def search_courses(request):
    query = request.GET.get('q', '').strip()

    courses = Course.objects.all()

    if query:
        courses = courses.filter(
            Q(course_name__icontains=query) |
            Q(category__icontains=query) |
            Q(career_field__icontains=query) |
            Q(skills__icontains=query)
        )

    return render(request, 'courses/search.html', {
        'courses': courses,
        'query': query
    })


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    return render(request, 'courses/course_detail.html', {
        'course': course
    })


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

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken.')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered.')

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                'Registration successful! You can now log in.'
            )

            return redirect('login')

    return render(request, 'courses/register.html')


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
            return redirect('home')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'courses/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect('home')