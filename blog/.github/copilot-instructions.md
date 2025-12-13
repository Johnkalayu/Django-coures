# AI Coding Guidelines for Django Blog Project

## Architecture Overview
This is a Django-based blog application with a modular structure:
- `blog/` - Main Django project settings and configuration
- `posts/` - App handling blog post functionality
- Uses SQLite database (`db.sqlite3`)

## Key Patterns
- **Data Handling**: Currently uses hardcoded lists in `posts/views.py` instead of Django models
- **Views**: Return raw HTML via `HttpResponse` rather than using templates
- **URLs**: Nested URL configuration with `posts.urls` included under `/post/`

## Development Workflow
- **Environment**: Activate virtual environment with `source coures/bin/activate`
- **Run Server**: `python manage.py runserver`
- **Database**: `python manage.py makemigrations` and `python manage.py migrate` (when models are added)
- **Admin**: Access at `/admin/` after creating superuser with `python manage.py createsuperuser`

## Important Notes
- `posts` app is not yet added to `INSTALLED_APPS` in `settings.py` - add `'posts'` to enable migrations and admin
- Views in `posts/views.py` have syntax errors (missing commas in dicts, typos like 'herf' instead of 'href')
- No models defined yet - plan to create `Post` model with fields like `title`, `content`, `created_at`

## Conventions
- Follow Django naming conventions for apps, models, and URLs
- Use class-based views for better maintainability (current views are function-based)
- Implement proper template rendering instead of inline HTML