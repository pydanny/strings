from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.rst').read()

import stringtheory

setup(
    name='strings',
    version=strings.__version__,
    description="Python strings for humans.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python',
    author=strings.__author__,
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/stringtheory',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)