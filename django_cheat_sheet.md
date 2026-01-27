# Django Commands Cheat Sheet

## 1. Starting a Django Project
| Command | Description |
| ------- | ----------- |
| `django-admin startproject <project_name>` | Create a new Django project |
| `cd <project_name>` | Change to the project directory |
| `python manage.py runserver` | Start the development server on default port (8000) |
| `python manage.py runserver <port>` | Start the server on a specific port |
| `python manage.py startapp <app_name>` | Create a new Django app within the project |

## 2. Working with Models and Migrations
| Command | Description |
| ------- | ----------- |
| `python manage.py makemigrations` | Detect changes in models and prepare migration files |
| `python manage.py migrate` | Apply migrations and create/update database schema |
| `python manage.py sqlmigrate <app_name> <migration_number>` | Show the SQL for a specific migration |
| `python manage.py showmigrations` | List all migrations and their current status |
| `python manage.py migrate <app_name>` | Apply migrations for a specific app |
| `python manage.py migrate <app_name> <migration_number>` | Apply migrations up to a specific migration |
| `python manage.py migrate <app_name> zero` | Unapply all migrations for an app |
| `python manage.py makemigrations --empty <app_name>` | Create an empty migration file |

## 3. Creating and Managing Users
| Command | Description |
| ------- | ----------- |
| `python manage.py createsuperuser` | Create a new superuser for the Django admin interface |
| `python manage.py changepassword <username>` | Change a user's password |

## 4. Django Shell and Database Shell
| Command | Description |
| ------- | ----------- |
| `python manage.py shell` | Open the interactive Django shell with models preloaded |
| `python manage.py shell_plus` | Enhanced shell with auto-loaded models (requires django-extensions) |
| `python manage.py dbshell` | Open the database shell for executing SQL commands directly |

## 5. Managing Database and Data
| Command | Description |
| ------- | ----------- |
| `python manage.py dumpdata` | Export all data from database to JSON |
| `python manage.py dumpdata <app_name>` | Export data from specific app |
| `python manage.py dumpdata <app_name>.<model_name>` | Export data from a specific model |
| `python manage.py dumpdata --indent 2 > data.json` | Export with formatting |
| `python manage.py loaddata <file_name>` | Load data from a JSON fixture file into the database |
| `python manage.py flush` | Remove all data from the database |
| `python manage.py inspectdb` | Generate model code based on an existing database schema |
| `python manage.py sqlflush` | Show the SQL that will be used to flush the database |

## 6. Testing
| Command | Description |
| ------- | ----------- |
| `python manage.py test` | Run the Django test suite for all apps |
| `python manage.py test <app_name>` | Run tests for a specific app |
| `python manage.py test <app_name>.<TestClass>` | Run a specific test case |
| `python manage.py test <app_name>.<TestClass>.<test_method>` | Run a specific test method |
| `python manage.py test --verbosity=2` | Run tests with detailed output |
| `python manage.py test --parallel` | Run tests in parallel |
| `python manage.py test --keepdb` | Preserve test database between runs |

## 7. Static Files
| Command | Description |
| ------- | ----------- |
| `python manage.py collectstatic` | Collect all static files into STATIC_ROOT directory for production |
| `python manage.py collectstatic --noinput` | Collect without prompting for confirmation |
| `python manage.py findstatic <file_name>` | Find the location of a specific static file |

## 8. Sessions and Cache Management
| Command | Description |
| ------- | ----------- |
| `python manage.py clearsessions` | Remove expired sessions from the database |
| `python manage.py clearcache` | Clear the cache (if using Django cache framework) |

## 9. Custom Management Commands
| Command | Description |
| ------- | ----------- |
| `python manage.py <custom_command>` | Run your custom management command |

To create a custom command, create:
```
<app_name>/management/commands/<command_name>.py
```

Example custom command:
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of your command'
    
    def add_arguments(self, parser):
        parser.add_argument('arg_name', type=str, help='Argument description')
    
    def handle(self, *args, **options):
        # Command logic here
        self.stdout.write(self.style.SUCCESS('Command executed successfully'))
```

## 10. Project Configuration and Debugging
| Command | Description |
| ------- | ----------- |
| `python manage.py check` | Check project for potential issues (e.g., missing migrations, improper configurations) |
| `python manage.py check --deploy` | Check project for security and deployment issues |
| `python manage.py diffsettings` | Show differences between current settings and Django defaults |

## 11. Internationalization and Localization
| Command | Description |
| ------- | ----------- |
| `python manage.py makemessages -l <language_code>` | Create translation files for a specific language (e.g., `-l en` for English) |
| `python manage.py makemessages -a` | Create/update translation files for all languages |
| `python manage.py compilemessages` | Compile translation files into `.mo` files |

## 12. Django Extensions (Optional Package)

Install with: `pip install django-extensions`

| Command | Description |
| ------- | ----------- |
| `python manage.py shell_plus` | Enhanced shell with all models imported |
| `python manage.py show_urls` | Display all URL patterns in the project |
| `python manage.py graph_models -a -o models.png` | Generate model diagram |
| `python manage.py runserver_plus` | Enhanced development server with Werkzeug debugger |
| `python manage.py reset_db` | Reset database to initial state |
| `python manage.py sqldiff` | Show SQL differences between models and database |

## 13. Working with Django Admin

### Registering Models in admin.py
```python
from django.contrib import admin
from .models import MyModel

# Simple registration
admin.site.register(MyModel)

# Custom admin class
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
```

## 14. URLs and Routing

### urls.py Patterns
```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('api/', include('api.urls')),
]
```

## 15. Common Model Operations in Shell

```python
# Import model
from myapp.models import MyModel

# Create object
obj = MyModel.objects.create(field1='value1', field2='value2')

# Get all objects
all_objects = MyModel.objects.all()

# Filter objects
filtered = MyModel.objects.filter(field1='value')

# Get single object
obj = MyModel.objects.get(pk=1)

# Update object
obj.field1 = 'new_value'
obj.save()

# Delete object
obj.delete()

# Bulk operations
MyModel.objects.filter(field1='value').update(field2='new_value')
MyModel.objects.filter(field1='value').delete()

# Aggregation
from django.db.models import Count, Avg, Sum
MyModel.objects.aggregate(total=Count('id'), average=Avg('price'))

# Annotations
MyModel.objects.annotate(item_count=Count('items'))
```

## 16. Environment Variables and Settings

### Using python-decouple
```python
# settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_URL = config('DATABASE_URL')
```

### Using django-environ
```python
# settings.py
import environ

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
DATABASES = {'default': env.db()}
```

## 17. Common Settings Patterns

### Development vs Production
```python
# settings/base.py - Common settings
# settings/development.py - Dev-specific settings
# settings/production.py - Prod-specific settings

# Run with specific settings
python manage.py runserver --settings=myproject.settings.development
```

### INSTALLED_APPS Order
```python
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    
    # Local apps
    'myapp',
]
```

## 18. Performance Tips

```bash
# Enable query logging
python manage.py runserver --settings=settings_with_debug_toolbar

# Profile database queries
from django.db import connection
print(len(connection.queries))
print(connection.queries)

# Use select_related for ForeignKey
MyModel.objects.select_related('foreign_key_field').all()

# Use prefetch_related for ManyToMany
MyModel.objects.prefetch_related('many_to_many_field').all()

# Use values/values_list for specific fields
MyModel.objects.values('field1', 'field2')
MyModel.objects.values_list('field1', flat=True)

# Use iterator() for large querysets
for obj in MyModel.objects.iterator():
    process(obj)
```

## 19. Deployment Checklist

```bash
# Security check
python manage.py check --deploy

# Collect static files
python manage.py collectstatic --noinput

# Compile messages
python manage.py compilemessages

# Run migrations
python manage.py migrate

# Create cache table (if using database cache)
python manage.py createcachetable
```

### Important Settings for Production
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 20. Common Troubleshooting

### Reset Migrations
```bash
# ⚠️ WARNING: DESTRUCTIVE OPERATION - Only use in DEVELOPMENT!
# ALWAYS backup your database and migration files before running these commands!

# 1. Backup migrations first (recommended)
cp -r */migrations /path/to/backup/

# 2. Delete all migration files except __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# 3. Drop database and recreate (or use flush)
python manage.py flush

# 4. Create fresh migrations
python manage.py makemigrations

# 5. Apply migrations
python manage.py migrate

# NOTE: Never do this in production! Use proper migration management instead.
```

### Fix "Table already exists" Error
```bash
# Fake initial migration
python manage.py migrate --fake-initial
```

### Debug Database Issues
```bash
# Show SQL for a migration
python manage.py sqlmigrate <app_name> <migration_number>

# Open database shell
python manage.py dbshell

# Inspect database
python manage.py inspectdb
```

