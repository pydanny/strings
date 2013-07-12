from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.rst').read()

import strings

setup(
    name='strings',
    version=strings.__version__,
    description="Python strings for humans.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python',
    author=strings.__author__,
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/strings',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)