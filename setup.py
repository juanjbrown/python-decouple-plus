# coding: utf-8
import os

from setuptools import setup


README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='python-decouple-plus',
    version='1.0.0',
    description='Addons for python-decouple',
    long_description=open(README).read(),
    author="Juan J. Brown",
    license="MIT",
    py_modules=['decouple_plus'],
    zip_safe=False,
    platforms='any',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    url='http://github.com/juanjbrown/python-decouple-plus/')
