from django.contrib import admin


from myapp.models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  

admin.site.register(Employees, EmployeesAdmin)



# admin.py in Django is used to register models with the Django admin interface, allowing for easy management and manipulation of application data through a web-based administrative interface.

# Typical use cases and reasons for using admin.py:

# 1. Model Registration:
# Admin.py is where you register your application's models to make them accessible via the Django admin interface. By registering models, you enable administrators to view, create, edit, and delete model instances through the admin site.

# 2. Customization:
# Admin.py allows you to customize the behavior and appearance of model admin interfaces. You can specify which fields are displayed, configure search and filtering options, define list and detail views, and add custom actions or behaviors.

# 3. Permissions and Security:
# Admin.py provides mechanisms for managing permissions and access control. You can specify who has access to view, edit, or delete model instances based on user roles and permissions defined in Django's authentication system.

# 4. Integration with Inline Models:
# Admin.py supports inline model editing, allowing you to edit related models directly within the parent model's admin interface. This is useful for managing related data without navigating to separate admin pages.

# 5. Automatic CRUD Interface:
# By default, Django's admin interface automatically generates CRUD (Create, Read, Update, Delete) interfaces for registered mod
