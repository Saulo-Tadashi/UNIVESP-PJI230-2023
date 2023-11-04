#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

def main():

    if 'WEBSITE_HOSTNAME' not in os.environ:
        print("Loading environment variables for .env file")
        load_dotenv('./.env')

    #settings_module = "Zotake_PI2.production" if 'WEBSITE_HOSTNAME' in os.environ else 'Zotake_PI2.settings'
    
    settings_module = "Zotake_PI2.production"

    if os.getenv('PRODUCTION') == False :
        settings_module = "Zotake_PI2.settings"

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
