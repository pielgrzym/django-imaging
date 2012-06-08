import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except:
        pass

setup(
        name = "django-imaging",
        version = "1.0.0",
        author = "Jakub Nawalaniec",
        author_email = "pielgrzym@prymityw.pl",
        description = ("AJAX driven gallery field for django"),
        license = "GNU GPL v2",
        keywords = "django",
        url = "https://github.com/pielgrzym/django-imaging",
        packages = find_packages(),
        zip_safe = False,
        include_package_data=True,
        long_description = read("README.txt"),
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Framework :: Django",
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            ],
        install_requires = [
            'django>=1.2',
            'pil',
            'django-imagekit>=1.0',
            ]
        )
