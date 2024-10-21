
# Django Commands Cheat Sheet

## 1. Starting a Django Project
| Command | Description |
| ------- | ----------- |
| `django-admin startproject <project_name>` | Create a new Django project |
| `cd <project_name>` | Change to the project directory |
| `python manage.py runserver` | Start the development server |
| `python manage.py startapp <app_name>` | Create a new Django app within the project |

## 2. Working with Models
| Command | Description |
| ------- | ----------- |
| `python manage.py makemigrations` | Detect changes in models and prepare migration files |
| `python manage.py migrate` | Apply migrations and create database schema |
| `python manage.py sqlmigrate <app_name> <migration_number>` | Show the SQL for a specific migration |
| `python manage.py showmigrations` | List migrations and their current status |

## 3. Creating and Managing Superusers
| Command | Description |
| ------- | ----------- |
| `python manage.py createsuperuser` | Create a new superuser for the Django admin interface |
| `python manage.py changepassword <username>` | Change a user's password |

## 4. Running the Development Server
| Command | Description |
| ------- | ----------- |
| `python manage.py runserver` | Start the development server on the default port (8000) |
| `python manage.py runserver <port>` | Start the server on a specific port (e.g., `python manage.py runserver 8080`) |
| `python manage.py runserver <ip_address:port>` | Start the server on a specific IP and port (e.g., `127.0.0.1:8000`) |

## 5. Managing Database
| Command | Description |
| ------- | ----------- |
| `python manage.py dbshell` | Open the database shell for executing SQL commands directly |
| `python manage.py dumpdata <app_name>.<model_name>` | Export data from a model to a JSON file |
| `python manage.py loaddata <file_name>` | Load data from a JSON fixture file into the database |

## 6. Working with Django Shell
| Command | Description |
| ------- | ----------- |
| `python manage.py shell` | Open the interactive Python shell with Django preloaded |
| `python manage.py shell_plus` | Open a shell with auto-loaded models and variables (if using `django-extensions`) |

## 7. Testing
| Command | Description |
| ------- | ----------- |
| `python manage.py test` | Run the Django test suite for all apps |
| `python manage.py test <app_name>` | Run tests for a specific app |
| `python manage.py test <app_name>.<TestClass>` | Run a specific test case |
| `python manage.py test --verbosity=2` | Run tests with detailed output |

## 8. Collecting Static Files
| Command | Description |
| ------- | ----------- |
| `python manage.py collectstatic` | Collect all static files into the `STATIC_ROOT` directory for production |
| `python manage.py findstatic <file_name>` | Find the location of a specific static file |

## 9. Working with Migrations
| Command | Description |
| ------- | ----------- |
| `python manage.py migrate <app_name>` | Apply migrations for a specific app |
| `python manage.py migrate <app_name> <migration_number>` | Apply up to a specific migration |
| `python manage.py showmigrations <app_name>` | Show migrations for a specific app |
| `python manage.py sqlflush` | Show the SQL that will be used to flush the database |

## 10. Clearing and Managing Cache
| Command | Description |
| ------- | ----------- |
| `python manage.py clearcache` | Clear the cache (if using Django cache framework) |

## 11. Creating Custom Management Commands
| Command | Description |
| ------- | ----------- |
| `python manage.py <custom_command>` | Run your custom management command (created inside the `management/commands/` folder in any app) |

## 12. Debugging
| Command | Description |
| ------- | ----------- |
| `python manage.py diffsettings` | Show differences between the current settings and Django defaults |
| `python manage.py check` | Check for potential issues in your project (e.g., missing migrations, improper configurations) |

## 13. Managing Translations
| Command | Description |
| ------- | ----------- |
| `python manage.py makemessages -l <language_code>` | Create translation files for a specific language (e.g., `-l en` for English) |
| `python manage.py compilemessages` | Compile translation files into `.mo` files |

