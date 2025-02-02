# FAQ Translation API

This project is a Django-based API for handling Frequently Asked Questions (FAQs) with support for translations in multiple languages. It leverages the **Django REST Framework (DRF)** for the API endpoints and uses the **Google Translate API** for translating questions into different languages.

## Features

- **Create, Read, Update, Delete (CRUD) FAQs**: Manage FAQs with the ability to add, view, update, and delete questions and answers.
- **Multi-language Support**: Automatically translate questions into Hindi and Bengali if translations are not provided.
- **Caching**: Translations are cached for faster access and to reduce external API calls to the translation service using `redis`.
- **Rich Text Answers**: Answers can be stored in rich text format using `django-ckeditor`.
- **Custom API Endpoint**: A custom `list` method in the FAQ viewset that retrieves translated questions based on a language query parameter (`lang`).
- **Admin Portal**: A web-based interface to manage FAQs, accessible at `/admin/`.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A toolkit for building Web APIs.
- **Google Translate API**: Used for translating FAQ questions into different languages.
- **Redis**: Caching layer for storing translations.
- **django-ckeditor**: Rich text editor for the answers.
- **pytest**: Used for running tests on the Django application.

## Setup

### Requirements

- **Python 3.x**
- **Redis**: Ensure Redis is installed and running. It is used for caching translations.
- **Django**: Version 3.x or above.
- **Django REST Framework**: For building RESTful APIs.
- **googletrans**: For translating FAQ questions.
- **django-ckeditor**: Rich text editor.

### Installation

#### **For Debian-based Linux (Recommended)**

If you're using a **Debian-based Linux** system, you can simplify the setup by running the `setup.sh` script:

```bash
bash setup.sh
```

This will:

- Install Redis
- Create a Python virtual environment
- Install dependencies
- Apply database migrations

#### **Manual Setup**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Blazzzze/faq-api.git
   cd faq-api
   ```

2. **Set up a virtual environment and install dependencies**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   If this doesn't work for you, please refer to <https://docs.python.org/3/library/venv.html> for more information on setting up a virtual environment.

3. **Install Redis**:

   ```bash
   sudo apt-get install redis-server
   sudo systemctl start redis-server
   ```

   If this doesn't work for you, please refer to <https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/> for more information on setting up redis-server.

4. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser for Admin Portal**:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

6. **Start the development server**:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

### Admin Portal

The **Admin Portal** is available at:

```
http://127.0.0.1:8000/admin/
```

- **Login using the credentials created with `createsuperuser`**.
- From the admin panel, you can manage FAQs easily using a user-friendly interface.
- **Supports WYSIWYG editing** for answers using CKEditor.

### Running Tests

Run the tests:

```bash
pytest
```

To run a specific test file:

```bash
pytest faq/tests/test_views.py
```

### Custom Shell Scripts

- **start.sh**: This script activates the virtual environment and starts the Django development server. You can use it to start the server in an isolated environment.
- **setup.sh**: This script installs Redis, sets up Python dependencies, and prepares the environment. **This script only supports Debian-based Linux**.

#### Usage of Shell Scripts

1. To run the server with `start.sh`:

   ```bash
   bash start.sh
   ```

2. To set up the project with `setup.sh`:

   ```bash
   bash setup.sh
   ```

### API Documentation

- **GET /api/faqs**: Retrieves all FAQs.
  - **Query parameter**: `lang` (optional, default is `en`).
  - **Response**: A list of FAQs with the translated questions in the specified language (if available).

  Example:

  ```bash
  GET /api/faqs?lang=hi
  ```

  The response will contain the FAQ list with questions translated into Hindi if they exist.

### Example Models and Views

- **FAQ Model**: Stores the question and answer for each FAQ, with optional fields for translations in Hindi and Bengali.
  
- **FAQSerializer**: Converts FAQ model instances to JSON format for API responses.

- **FAQViewSet**: A custom viewset to manage FAQ objects and return translations based on the `lang` query parameter.

### Caching and Translations

- **`translate_text()`**: Uses the Google Translate API to translate questions.
- **`get_cached_translation()`**: Retrieves translations from the cache or generates and caches them if not present.

With these changes, your setup process is now streamlined, the admin portal is clearly mentioned, and Debian users can quickly get started with the `setup.sh` script. 🚀
