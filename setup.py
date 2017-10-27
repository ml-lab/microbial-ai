#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='microbial_ai',
    version='0.1.0',
    description=("Microbial growth simulation incorporating adaptation "
                 "through reinforcement learning"),
    long_description=readme + '\n\n' + history,
    author="Dileep Kishore",
    author_email='dkishore@bu.edu',
    url='https://github.com/dileep-kishore/microbial_ai',
    packages=find_packages(include=['microbial_ai']),
    entry_points={
        'console_scripts': [
            'microbial_ai=microbial_ai.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='microbial_ai',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
