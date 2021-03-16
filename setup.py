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

from setuptools import find_packages
from setuptools import setup


def _read(fname):
    with open(fname) as fp:
        return fp.read()


setup(name='Products.StandardCacheManagers',
      version='4.1.0',
      url='https://github.com/zopefoundation/Products.StandardCacheManagers',
      project_urls={
          'Issue Tracker': ('https://github.com/zopefoundation'
                            '/Products.StandardCacheManagers/issues'),
          'Sources': ('https://github.com/zopefoundation'
                      '/Products.StandardCacheManagers'),
      },
      license='ZPL 2.1',
      description="Cache managers for Zope",
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description=_read('README.rst') + '\n' + _read('CHANGES.rst'),
      packages=find_packages('src'),
      namespace_packages=['Products'],
      package_dir={'': 'src'},
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Framework :: Zope",
          "Framework :: Zope :: 4",
          "Framework :: Zope :: 5",
          "License :: OSI Approved :: Zope Public License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: Implementation :: CPython",
      ],
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      install_requires=[
          'setuptools',
          'six',
          'AccessControl',
          'transaction',
          'Zope2 >= 4.0a5',
          'zope.component',
      ],
      include_package_data=True,
      zip_safe=False,
      )
