# Todo App with Google Drive Integration

This is a simple Django project that includes a Todo App with Google Drive integration.
Users can manage tasks through a RESTful API, and there is also an API endpoint to create documents in Google Drive.

## Setup

1. Clone the repository:

    ```bash
    git clone  https://github.com/344988/nova.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-todo-app
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    # On Windows
    .\venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to access the Todo App.

## API Endpoints

- **Task List and Create:**
    - Endpoint: `/tasks/`
    - Method: GET (list tasks), POST (create task)

- **Task Detail, Update, and Delete:**
    - Endpoint: `/tasks/<int:pk>/`
    - Method: GET (retrieve task), PUT (update task), DELETE (delete task)

- **Create Document in Google Drive:**
    - Endpoint: `/create-document/`
    - Method: POST
    - Parameters:
        - `data` (Text content of the file)
        - `name` (Name of the file)

## Google Drive Integration

To enable Google Drive integration, make sure to provide valid credentials and token files:
- `path/to/your/credentials.json` (Google Cloud Console credentials)
- `path/to/your/token.json` (Token file for storing access tokens)

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
