from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Employees(models.Model):
    name= models.CharField(max_length=200)
    
    email=models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.BigIntegerField()
    
    def __str__(self):
        return self.name  #this code we write for show the real name in the palece on object name
# Models in Django serve as the abstraction layer for interacting with your application's data. 
# They define the structure and behavior of your data models, representing tables in the database.

# Reasons for creating models in Django:

# 1. Data Representation:
# Models define the structure of your application's data. Each model class represents a table in the database, and its attributes represent the fields/columns of that table.

# 2. Data Validation:
# Models enforce data validation rules, ensuring that only valid data is saved to the database. You can specify field types, constraints, and validation logic in model definitions.

# 3. Database Interaction:
# Models provide an abstraction layer for database operations. They encapsulate database queries and CRUD (Create, Read, Update, Delete) operations, making it easier to interact with the database without writing raw SQL queries.

# 4. Relationships:
# Models define relationships between different types of data. Django supports various types of relationships, such as ForeignKey, OneToOneField, and ManyToManyField, allowing you to establish connections between related data entities.

# 5. Administration Interface:
# Django's built-in admin interface leverages models to provide a powerful CRUD interface for managing application data. Models define how data is displayed and manipulated in the admin interface.

# 6. Business Logic Separation:
# Models help in separating business logic from database-related concerns. They centralize data-related functionality, making the codebase more organized and maintainable.

# 7. ORM (Object-Relational Mapping):
# Django's ORM translates Python code into SQL queries, abstracting away the complexity of database interactions. Models provide a high-level interface for performing database operations in a Pythonic way.

# Overall, models play a crucial role in the Django framework by defining the structure, behavior, and interaction of your application's data, thus facilitating data management and persistence.
