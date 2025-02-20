#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')

test_requirements = ['pytest>=3', ]

setup(
    author="Gonzalo Alvarez",
    author_email='gonzaloab@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python AWS Client to get Access through the console based on a profile",
    entry_points={
        'console_scripts': [
            'pyawsah=awsah.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyawsah',
    name='pyawsah',
    packages=find_packages(include=['awsah', 'awsah.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/GonzaloAlvarez/pyawsah',
    version='0.1.0',
    zip_safe=False,
)
