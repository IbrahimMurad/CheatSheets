# Django Commands Cheat Sheet

## 1. Setting Up a Django Project
| Command | Description |
| ------- | ----------- |
| `django-admin startproject <project_name>` | Create a new Django project |
| `python manage.py startapp <app_name>` | Create a new app within your project |
| `python manage.py runserver` | Start the development server (default: http://127.0.0.1:8000/) |
| `python manage.py runserver <port_number>` | Start the server on a specified port |

## 2. Database Migrations
| Command | Description |
| ------- | ----------- |
| `python manage.py makemigrations` | Create migration files based on model changes |
| `python manage.py migrate` | Apply migrations to the database |
| `python manage.py sqlmigrate <app_name> <migration_number>` | Show the SQL statements for a specific migration |
| `python manage.py showmigrations` | List all migrations and their status |

## 3. Creating and Managing Superusers
| Command | Description |
| ------- | ----------- |
| `python manage.py createsuperuser` | Create a new superuser for the admin interface |

## 4. Django Shell
| Command | Description |
| ------- | ----------- |
| `python manage.py shell` | Open the interactive Django shell |
| `python manage.py dbshell` | Open the database shell for raw SQL queries |

## 5. Collecting Static Files
| Command | Description |
| ------- | ----------- |
| `python manage.py collectstatic` | Collect all static files into the `STATIC_ROOT` directory for deployment |

## 6. Running Tests
| Command | Description |
| ------- | ----------- |
| `python manage.py test` | Run tests for all apps |
| `python manage.py test <app_name>` | Run tests for a specific app |

## 7. Managing and Inspecting Models
| Command | Description |
| ------- | ----------- |
| `python manage.py inspectdb` | Generate model code based on an existing database schema |
| `python manage.py flush` | Remove all data from the database and reset migrations |

## 8. Managing User Sessions and Cache
| Command | Description |
| ------- | ----------- |
| `python manage.py clearsessions` | Remove expired sessions from the database |
| `python manage.py clearcache` | Clear the cache (if configured) |

## 9. Working with URLs
| Command | Description |
| ------- | ----------- |
| `python manage.py check` | Check the project for common issues |
| `python manage.py show_urls` | List all URLs (requires `django-extensions` package) |

## 10. Custom Commands (Advanced)
| Command | Description |
| ------- | ----------- |
| `python manage.py <custom_command>` | Run a custom management command you've created |

## 11. Deployment and Configuration
| Command | Description |
| ------- | ----------- |
| `python manage.py check --deploy` | Check the project for security and deployment issues |
| `python manage.py migrate --fake` | Mark a migration as applied without running it |
| `python manage.py diffsettings` | Show which settings have been changed from the default |

---

Use this cheat sheet as a quick reference while working on Django projects. Let me know if you need more detailed information about any command!
