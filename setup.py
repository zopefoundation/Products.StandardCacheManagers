##############################################################################
#
# Copyright (c) 2010 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from setuptools import setup, find_packages

setup(name='Products.StandardCacheManagers',
      version='4.0.0',
      url='http://pypi.python.org/pypi/Products.StandardCacheManagers',
      license='ZPL 2.1',
      description="Cache managers for Zope 2.",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=(open('README.rst').read() + '\n' +
                        open('CHANGES.rst').read()),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      install_requires=[
          'setuptools',
          'six',
          'AccessControl',
          'transaction',
          'Zope2 >= 4.0a1',
          'zope.component',
      ],
      include_package_data=True,
      zip_safe=False,
      )
