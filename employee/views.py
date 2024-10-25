from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from employee.models import Employee, EmployeeField
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')



def settings_view(request):
    fields = EmployeeField.objects.all()

    if request.method == 'POST':
        field_name = request.POST.get('field_name')
        EmployeeField.objects.create(name=field_name)
        return redirect('settings')

    return render(request, 'settings.html', {'fields': fields})

def edit_field_view(request, field_id):
    field = get_object_or_404(EmployeeField, id=field_id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        field.name = new_name
        field.save()
        return redirect('settings')
def delete_field_view(request, field_id):
    field = get_object_or_404(EmployeeField, id=field_id)

    if request.method == 'POST':
        field.delete()
        return redirect('settings')


def employee_list(request):
    """View to list employees along with their dynamic fields."""
    employees = Employee.objects.all()
    try:
        fields = EmployeeField.objects.all()
    except:
        fields = []
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Collect data for dynamic fields
        additional_data = {field.name: request.POST.get(field.name) for field in fields}
        print(name,email,phone,additional_data,'-----------')
        # Create the new employee with additional data
        Employee.objects.create(name=name, email=email, phone=phone, additional_data=additional_data)
        return redirect('employee_list')
    
    return render(request, 'employee_list.html', {'employees': employees, 'fields': fields})


def employee_create(request):
    """View to create a new employee with dynamic fields."""
    try:
        fields = EmployeeField.objects.all()
    except:
        fields = []
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Collect data for dynamic fields
        additional_data = {field.name: request.POST.get(field.name) for field in fields}
        print(name,email,phone,additional_data,'-----------')
        # Create the new employee with additional data
        Employee.objects.create(name=name, email=email, phone=phone, additional_data=additional_data)
        return redirect('employee_list')
    
    return render(request, 'employee_form.html', {'fields': fields})
