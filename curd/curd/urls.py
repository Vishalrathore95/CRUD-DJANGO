"""
URL configuration for curd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('Add/', views.Add,name='add'),
    path('Edit/', views.Edit,name='Edit'),
    path('Update/<str:id>', views.Update,name='Update'),
    path('Delete/<str:id>', views.Delete,name='Delete'),
    
]



# URLs in Django serve as the mapping between the requested URL paths and the corresponding views that handle those requests.

# Reasons for creating URLs in Django:

# 1. Routing Requests:
# URLs define the routes or endpoints of your web application. They specify which views should be invoked to handle specific URL patterns.

# 2. URL Configuration:
# URLs provide a centralized location to configure the URL patterns for different parts of your application. This allows for easy management and organization of your project's URL structure.

# 3. Decoupling:
# Separating URLs from views allows for better decoupling of the application components. Views can focus solely on handling request logic, while URLs handle routing and mapping.

# 4. Readability and Maintainability:
# Using explicit URL patterns in Django enhances the readability and maintainability of the codebase. Developers can easily understand the URL structure and map URLs to corresponding views.

# 5. Reusability:
# URL patterns can be reused across multiple views or applications within the project, promoting code reuse and modularity.

# 6. Parameter Passing:
# URLs support the passing of parameters or arguments from the URL path to the view functions, enabling dynamic content generation and customization.

# Overall, URLs play a crucial role in the Django framework by providing a mechanism for routing requests, configuring URL patterns, promoting decoupling, enhancing readability, and supporting code reuse and parameter passing.

