#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#импорт библиотек
import os
import sys

#основная функция - запуск административных команд
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketSite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#запуск main
if __name__ == '__main__':
    main()
