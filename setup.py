#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Drew E. Winters",
    author_email='drewEwinters@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Orthogonalize interactions by centering residuals",
    #entry_points={
    #    'console_scripts': [
    #        'resmod=resmod.cli:main',
    #    ],
    #},
    install_requires=[
        "numpy>=1.0",
        "pandas>=1.0",
        "statsmodels>=0.10.0"
        ],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['resmod',"interaction", "centered residuals"],
    name='resmod',
    packages=find_packages(include=['resmod', 'resmod.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/drewwint/resmod',
    version='0.1.4',
    zip_safe=False,
)
