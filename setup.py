#!/usr/bin/env python
from setuptools import setup
import slackme

repo_url = 'https://github.com/andreif/slackme'
version = slackme.__version__

setup(
    name='slackme',
    version=version,
    author='Andrei Fokau',
    author_email='andrei@5monkeys.se',
    description=slackme.parser.description,
    url=repo_url,
    download_url='%s/tarball/%s' % (repo_url, version),
    keywords=['slack', 'webhook'],
    license='BSD',
    zip_safe=False,
    py_modules=[
        'slackme',
    ],
    entry_points={
        'console_scripts': [
            'slackme = slackme:main',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
