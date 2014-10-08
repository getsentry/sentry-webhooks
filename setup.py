#!/usr/bin/env python
"""
sentry-webhooks
===============

An extension for Sentry which allows creation various web hooks.

:copyright: (c) 2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    # 'sentry>=7.0.0',
]

setup(
    name='sentry-webhooks',
    version='0.3.1',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/getsentry/sentry-webhooks',
    description='A Sentry extension which integrates web hooks.',
    long_description=__doc__,
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
       'sentry.apps': [
            'webhooks = sentry_webhooks',
        ],
       'sentry.plugins': [
            'webhooks = sentry_webhooks.plugin:WebHooksPlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
