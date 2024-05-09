# CRUD Data Table for Database with Modal Form

This project is a simple web application built using Bootstrap for front-end design, Django for backend functionalities, and SQLite for the database. It allows users to manage
employee data through CRUD (Create, Read, Update, Delete) operations.

## Screenshots

Here are some screenshots of the application:

- **Employee Management Page**: This screenshot shows the main page of the application where users can view, add, edit, and delete employee records.

  ![Employee Management Page])
![Screenshot 2024-05-09 141922](https://github.com/Vishalrathore95/CRUD-DJANGO/assets/138272471/00e037c7-c8db-4a94-a6db-f658625e8c0d)

- **Add Employee Modal**: This screenshot displays the modal form used for adding a new employee record.

  ![Add Employee Modal]()
![Screenshot 2024-05-09 141940](https://github.com/Vishalrathore95/CRUD-DJANGO/assets/138272471/133fda37-fdde-45c3-baa6-133b65a6c507)

- **Edit Employee Modal**: This screenshot shows the modal form used for editing an existing employee record.

  ![Edit Employee Modal]()
![Screenshot 2024-05-09 141959](https://github.com/Vishalrathore95/CRUD-DJANGO/assets/138272471/3d240e28-7319-495a-a4aa-8a638ffa5504)

- **Delete Confirmation Modal**: This screenshot illustrates the modal dialog used for confirming the deletion of an employee record.
![Screenshot 2024-05-09 142015](https://github.com/Vishalrathore95/CRUD-DJANGO/assets/138272471/00f54895-3363-46c6-bd71-a3e826f2cfc9)

  ![Delete Confirmation Modal](/)
![Screenshot 2024-05-09 142029](https://github.com/Vishalrathore95/CRUD-DJANGO/assets/138272471/f9a2f990-4267-4491-b2b5-0e079f279093)

## Features

- **Bootstrap Styling**: Utilizes Bootstrap for a responsive and visually appealing user interface.
- **CRUD Operations**: Allows users to perform CRUD operations on employee data, including adding, editing, and deleting records.
- **Modal Forms**: Utilizes modal forms for adding and editing employee information, providing a clean and intuitive user experience.
- **Database Integration**: Integrates with a SQLite database to store and manage employee records.
- **Pagination**: Provides pagination functionality to navigate through large sets of data.

## Installation

1. Clone the repository:

    ```bash
  [  git clone https://github.com/your_username/your_repository.git](https://github.com/Vishalrathore95/CRUD-DJANGO/tree/main/curd)
    ```

2. Navigate to the project directory:

    ```bash
    cd curd
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000/` in your web browser.

## Usage

- Upon accessing the application, you'll be presented with a table displaying existing employee records.
- To add a new employee, click on the "Add New Employee" button, fill in the required information in the modal form, and click "Add".
- To edit an existing employee record, click on the "Edit" icon next to the respective employee row. Update the information in the modal form and click "Update".
- To delete an employee record, click on the "Delete" icon next to the respective employee row. Confirm the action in the modal dialog.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Additional Information

### Views

Views in Django handle the logic of your web application. They are responsible for processing incoming requests from clients (e.g., web browsers) and returning appropriate responses.

- **Request Handling**: Views define functions or classes that handle different types of HTTP requests (e.g., GET, POST, PUT, DELETE) sent to your application's URLs.
- **Business Logic**: Views contain the business logic of your application. They process data, perform calculations, and make decisions based on the incoming request and application requirements.
- **Data Interaction**: Views interact with models to fetch or manipulate data stored in the database. They may query the database to retrieve specific data or save/update data based on the request.
- **Template Rendering**: Views render templates to generate HTML content dynamically. They pass data to templates, which are then rendered with the appropriate context to produce the final HTML output returned to the client.
- **Response Generation**: Views generate HTTP responses to send back to the client. These responses can include HTML content, JSON data, redirections, or error messages, depending on the requirements of the request.

### View Functions

#### index(request)

- Fetches all employee records from the database.
- Renders the 'index.html' template with the retrieved data.

#### Add(request)

- Handles the logic for adding a new employee record.
- Retrieves data from the POST request, creates a new `Employees` object, and saves it to the database.
- Redirects to the 'index' view after adding the record.

#### Edit(request)

- Redirects to the 'index' view. (This function doesn't appear to serve any specific functionality.)

#### Update(request, id)

- Handles the logic for updating an existing employee record.
- Retrieves data from the POST request, finds the `Employees` object with the specified ID, updates its fields, and saves the changes to the database.
- Redirects to the 'index' view after updating the record.

#### Delete(request, id)

- Handles the logic for deleting an existing employee record.
- Retrieves the `Employees` object with the specified ID, deletes it from the database, and redirects to the 'index' view.
