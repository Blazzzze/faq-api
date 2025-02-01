# FAQ Translation API

This project is a Django-based API for handling Frequently Asked Questions (FAQs) with support for translations in multiple languages. It leverages the **Django REST Framework (DRF)** for the API endpoints and uses the **Google Translate API** for translating questions into different languages.

## Features

- **Create, Read, Update, Delete (CRUD) FAQs**: Manage FAQs with the ability to add, view, update, and delete questions and answers.
- **Multi-language Support**: Automatically translate questions into Hindi and Bengali if translations are not provided.
- **Caching**: Translations are cached for faster access and to reduce external API calls to the translation service using `redis`.
- **Rich Text Answers**: Answers can be stored in rich text format using `django-ckeditor`.
- **Custom API Endpoint**: A custom `list` method in the FAQ viewset that retrieves translated questions based on a language query parameter (`lang`).

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

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Blazzzze/faq-api.git
   cd faq-api
   ```

2. **Install dependencies**:
   - Install Python dependencies:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

   - Install Redis:
     Follow the [Redis installation guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/#connect-to-redis) to install Redis.

3. **Setup Redis**:
   - Ensure Redis is installed and running.
   - If you are using Ubuntu, you can install Redis with:

     ```bash
     sudo apt-get install redis-server
     sudo systemctl start redis-server
     ```

4. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

### Running Tests

Run the tests:

```bash
pytest
```

To run a specific test file:

```bash
pytest faq/test_views.py
```

### Custom Shell Scripts

- **start.sh**: This script activates the virtual environment and starts the Django development server. You can use it to start the server in an isolated environment.
- **setup.sh**: This script installs Redis, sets up Python dependencies, and prepares the environment. **This script only supports debian based linux**.

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
