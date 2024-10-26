from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from employee.models import Employee, EmployeeField
from .forms import SignupForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect('employee_list')
        else:
            messages.error(request, form.errors)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def dashboard(request):
    return render(request, 'employee_list.html')


@login_required(login_url='login')
def settings_view(request):
    fields = EmployeeField.objects.all()

    if request.method == 'POST':
        field_name = request.POST.get('field_name')
        EmployeeField.objects.create(name=field_name)
        return redirect('settings')

    return render(request, 'settings.html', {'fields': fields})

@login_required(login_url='login')
def edit_field_view(request, field_id):
    field = get_object_or_404(EmployeeField, id=field_id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        field.name = new_name
        field.save()
        return redirect('settings')

@login_required(login_url='login')
def delete_field_view(request, field_id):
    field = get_object_or_404(EmployeeField, id=field_id)

    if request.method == 'POST':
        field.delete()
        return redirect('settings')


@login_required(login_url='login')
def employee_list(request):

    """
    This view handles the employee list page. It displays all employees and 
    employee fields. It also handles POST and PATCH requests for creating and 
    updating employees, respectively.

    :param request: The request object
    :return: The rendered employee list page
    """
    employees = Employee.objects.all()
    fields = EmployeeField.objects.all()

    if request.method in ['POST', 'PATCH']:
        employee_data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'additional_data': {field.name: request.POST.get(field.name) for field in fields}
        }

        if request.method == 'POST':
            Employee.objects.create(**employee_data)
        elif request.method == 'PATCH':
            Employee.objects.filter(id=request.POST.get('id')).update(**employee_data)

        return redirect('employee_list')

    return render(request, 'employee_list.html', {'employees': employees, 'fields': fields})
