# toDoList
This to-do list application is built using Django, a high-level Python web framework. The application's structure includes:

1. **Models**: Defined in `todos/models.py`, where `TodoItem` is the main model with fields for `title` and `completed`.

2. **URLs**: Configured in `mytodolist/urls.py` and `todos/urls.py`. The main application routes include paths to view the list of to-dos, add a new to-do, and mark a to-do as complete.

3. **Views**: Located in `todos/views.py`, these handle the logic for displaying the to-do list, adding new to-dos, and updating to-dos as completed.

4. **Templates**: The `todos/todo_list.html` template renders the to-do items and includes forms for adding new items and marking existing items as complete.

This setup allows for a simple yet functional to-do list web application.
