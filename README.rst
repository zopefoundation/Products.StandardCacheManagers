.. image:: https://github.com/zopefoundation/Products.StandardCacheManagers/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/Products.StandardCacheManagers/actions/workflows/tests.yml

.. image:: https://coveralls.io/repos/github/zopefoundation/Products.StandardCacheManagers/badge.svg?branch=master
    :target: https://coveralls.io/github/zopefoundation/Products.StandardCacheManagers?branch=master

.. image:: https://img.shields.io/pypi/v/Products.StandardCacheManagers.svg
    :target: https://pypi.org/project/Products.StandardCacheManagers/
    :alt: Current version on PyPI

.. image:: https://img.shields.io/pypi/pyversions/Products.StandardCacheManagers.svg
    :target: https://pypi.org/project/Products.StandardCacheManagers/
    :alt: Supported Python versions

Overview
========

This package provides two cache managers for Zope. A RAMCacheManager and an
Accelerated HTTP cache manager, which adds HTTP cache headers to responses.

The following is intended for people interested in the internals of
RAMCacheManager, such as maintainers.

Introduction
============

The caching framework does not interpret the data in any way, it acts
just as a general storage for data passed to it.  It tries to check if
the data is pickleable though.  IOW, only pickleable data is
cacheable. 

The idea behind the RAMCacheManager is that it should be shared between
threads, so that the same objects are not cached in each thread.  This
is achieved by storing the cache data structure itself as a module
level variable (RAMCacheManager.caches).  This, of course, requires
locking on modifications of that data structure.

Each RAMCacheManager instance has one cache in RAMCacheManager.caches
dictionary.   A unique __cacheid is generated when creating a cache
manager and it's used as a key for caches.

Object Hierarchy
================

RAMCacheManager
  RAMCache
    ObjectCacheEntries
      CacheEntry

RAMCacheManager is a persistent placeful object.  It is assigned a
unique __cacheid on its creation.  It is then used as a key to look up
the corresponding RAMCache object in the global caches dictionary.
So, each RAMCacheManager has a single RAMCache related to it.

RAMCache is a volatile cache, unique for each RAMCacheManager.  It is
shared among threads and does all the locking.  It has a writelock.
No locking is done on reading though.  RAMCache keeps a dictionary of
ObjectCacheEntries indexed by the physical path of a cached object.

ObjectCacheEntries is a container for cached values for a single object.  
The values in it are indexed by a tuple of a view_name, interesting 
request variables, and extra keywords passed to Cache.ZCache_set(). 

CacheEntry is a wrapper around a single cached value.  It stores the
data itself, creation time, view_name and keeps the access count.
