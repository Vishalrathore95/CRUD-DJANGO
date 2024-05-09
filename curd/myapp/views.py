from django.shortcuts import render,redirect, get_object_or_404
from myapp.models import Employees



# Views in Django handle the logic of your web application.
# They are responsible for processing incoming requests from clients (e.g., web browsers) and returning appropriate responses.

# Reasons for creating views in Django:

# 1. Request Handling:
# Views define functions or classes that handle different types of HTTP requests (e.g., GET, POST, PUT, DELETE) sent to your application's URLs.

# 2. Business Logic:
# Views contain the business logic of your application. They process data, perform calculations, and make decisions based on the incoming request and application requirements.

# 3. Data Interaction:
# Views interact with models to fetch or manipulate data stored in the database. They may query the database to retrieve specific data or save/update data based on the request.

# 4. Template Rendering:
# Views render templates to generate HTML content dynamically. They pass data to templates, which are then rendered with the appropriate context to produce the final HTML output returned to the client.

# 5. Response Generation:
# Views generate HTTP responses to send back to the client. These responses can include HTML content, JSON data, redirections, or error messages, depending on the requirements of the request.

# Overall, views play a crucial role in the Django framework by encapsulating the logic needed to handle requests and generate responses, thus enabling the development of dynamic and interactive web applications.



def index(request):
    emp = Employees.objects.all()
    context ={
        "emp":emp
    }
    return render(request,'index.html',context)



def Add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        
        en = Employees(name=name, email=email, address=address, phone=phone)
        en.save()
    
    return redirect('index')

    
def Edit(request):
    emp = Employees.objects.all()
    context={
        "emp":emp
    }
    return redirect( request,'index.html',context)



def Update(request,id):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        
        en = Employees( id=id,name=name, email=email, address=address, phone=phone)
        en.save()
    
    return redirect('index')




def Delete(request, id):
    employee = get_object_or_404(Employees, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('index')  # Assuming your index view name is 'index'
    return redirect('index')  