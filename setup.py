#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='ulp',
            version='1.0.0',
            author='Guilherme Victal',
            author_email='guilherme at victal.eti.br',
            url='https://github.com/victal/ulp',
            description='ULP is a Locator Picker - a PathPicker clone for URLs',
            license='MIT',
            packages=['ulp'],
            requires=['pyperclip', 'urwid'],
            entry_points={
                  'console_scripts': [
                        'ulp=ulp.cli:main'
                        ]
                  },
            classifiers=[
                  # How mature is this project? Common values are
                  #   3 - Alpha
                  #   4 - Beta
                  #   5 - Production/Stable
                  'Development Status :: 3 - Alpha',

                  # Indicate who your project is intended for
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Build Tools',

                  # Pick your license as you wish (should match "license" above)
                  'License :: OSI Approved :: MIT License',

                  # Specify the Python versions you support here. In particular, ensure
                  # that you indicate whether you support Python 2, Python 3 or both.
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.2',
                  'Programming Language :: Python :: 3.3',
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
                  ]
            )
