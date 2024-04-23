#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# import threading

# from arena import views

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arenaGame.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # background_thread = threading.Thread(target=views.runGames)
    # background_thread.daemon = True
    # background_thread.start()
    # views.updateDB()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
