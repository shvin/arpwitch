#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='arpwitch',
    version='2018.2',
    description='A modern arpwatch tool',
    long_description='A modern arpwatch tool with JSON formatted oututs and easy options to exec commands when network changes are observed.',

    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Networking :: Monitoring',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='arpwitch arpwatch arp network',

    author='Verb Networks Pty Ltd',
    author_email='contact@verbnetworks.com',
    url='https://github.com/verbnetworks/arpwitch',
    license='Apache',

    packages=['arpwitch'],
    scripts=['bin/arpwitch'],
    install_requires=['scapy-python3'],

)
