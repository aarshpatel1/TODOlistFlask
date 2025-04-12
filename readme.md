# Flask To-Do Application

This is a simple To-Do application built using Flask, Flask-Bootstrap, Flask-WTF, and SQLAlchemy. The app allows users to add, edit, and delete tasks.

## Features

- Add new tasks with a title.
- Edit existing tasks.
- Delete tasks.
- Tasks are stored in a SQLite database.
- Responsive design using Bootstrap 5.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite
- **Forms**: Flask-WTF

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure

- `main.py`: The main application file.
- `templates/`: Contains HTML templates for the app.
  - `base.html`: Base template for the app.
  - `todo.html`: Template for displaying and managing tasks.
- `static/`: Contains static files like CSS and JavaScript.

## Dependencies

- Flask
- Flask-Bootstrap
- Flask-WTF
- Flask-SQLAlchemy
- WTForms

## Database Schema

The app uses a single table `Todos` with the following fields:
- `id`: Primary key.
- `todo`: Task title (unique and required).
- `date`: Date the task was created.
- `time`: Time the task was created.
- `description`: Optional description of the task.

