#!/usr/bin/env python

import os
import sys
import django

from django.conf import settings
from django.test.runner import DiscoverRunner
from django.core.management import execute_from_command_line


if not settings.configured:
    settings_dict = dict(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django_pandas',
            'import_export_pandas.tests.testapp',
        ),
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
                "USER": "",
                "PASSWORD": "",
                "HOST": "",
                "PORT": "",
            }
        },
        MIDDLEWARE_CLASSES=()
    )

    settings.configure(**settings_dict)
    django.setup()


def main(*test_args):
    if not test_args:
        test_args = ['import_export_pandas']

        parent = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, parent)

        failures = DiscoverRunner(
            verbosity=1, interactive=True, failfast=False).run_tests(test_args)
        sys.exit(failures)
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main(*sys.argv[1:])
