"""Setup script of iep"""
from setuptools import setup, find_packages
import import_export_pandas as iep


def read(filename):
    with open(filename) as fd:
        return fd.read()

setup(
    name='django-import-export-pandas',
    version=iep.__version__,
    description=iep.__doc__,
    long_description=read('README.rst'),
    keywords=['import', 'export', 'dataframe'],
    author=iep.__author__,
    author_email=iep.__email__,
    url=iep.__url__,

    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=iep.__license__,
    zip_safe=False,
    # install_requires=read('requirements.txt').splitlines(),
)
