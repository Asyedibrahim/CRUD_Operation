from django.shortcuts import render,redirect
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your views here.
def home(request):
    return render(request,'home.html')

# Code For add_employee
def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})

# Code For show_employee
def show(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

# Code For edit
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html' , {'employee':employee})

# Code For Update
def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html' , {'employee':employee})
    

# Code For delete
def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")




