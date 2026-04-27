from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import ExamForm
from .forms import ExamFormForm


def is_admin(user):
    return user.is_staff


# LOGIN
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid credentials")
    return render(request, 'login.html')


# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created")
        return redirect('login')

    return render(request, 'signup.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# DASHBOARD
@login_required
def dashboard(request):
    forms = ExamForm.objects.all().order_by('-created_at')

    return render(request, 'dashboard.html', {
        'forms': forms,
        'total': forms.count(),
        'approved': forms.filter(status='approved').count(),
        'pending': forms.filter(status='pending').count(),
    })


# USER FORM
@login_required
def fill_form(request):
    if request.user.is_staff:
        return redirect('dashboard')

    if ExamForm.objects.filter(user=request.user).exists():
        return render(request, 'already_submitted.html')

    if request.method == 'POST':
        form = ExamFormForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Form submitted")
            return redirect('dashboard')
    else:
        form = ExamFormForm()

    return render(request, 'form.html', {'form': form})


# EDIT (ADMIN)
@login_required
@user_passes_test(is_admin)
def edit_form(request, id):
    obj = get_object_or_404(ExamForm, id=id)

    if request.method == 'POST':
        form = ExamFormForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated")
            return redirect('dashboard')
    else:
        form = ExamFormForm(instance=obj)

    return render(request, 'form.html', {'form': form})


# ACTIONS
@login_required
@user_passes_test(is_admin)
@require_POST
def approve_form(request, id):
    obj = get_object_or_404(ExamForm, id=id)
    obj.status = 'approved'
    obj.save()
    return redirect('dashboard')


@login_required
@user_passes_test(is_admin)
@require_POST
def reject_form(request, id):
    obj = get_object_or_404(ExamForm, id=id)
    obj.status = 'rejected'
    obj.save()
    return redirect('dashboard')


@login_required
@user_passes_test(is_admin)
@require_POST
def delete_form(request, id):
    obj = get_object_or_404(ExamForm, id=id)
    obj.delete()
    return redirect('dashboard')