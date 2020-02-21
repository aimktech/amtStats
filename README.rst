amtStats
========

|license| |python| |pypi| |build| |coverage|

----

*amtStats* is a Python 3 package that provides a very simplistic statistics
on a dataset. It does not require the use of `Numpy`_.

The following statistics are available:
    - **min**
    - **max**
    - **sum**
    - **count**
    - **mean**
    - **median**
    - **stddev**
    - **quantile**: Q1, Q3, InterQuantile Range (IQR)
    - **percentiles**: 10th, 30th, 50th, 70th, 90th, 95th, 97th and 99th

----

Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install amtstats

Import the ``Statistics`` class in your python code and then instantiate it.

.. code:: python

    from amtStats import Statistics
    myStats = Statistics()


Use ``update`` to add numbers (*int* or *float*) to the data set.

.. code:: python

    # add some integer numbers
    for i in range(100):
        myStats.update(random.randint(1, 1000))

    # and some float
    for i in range(50):
        myStats.update(random.random()*100)


Use ``compute`` to compute the statistics for the dataset.
The result is returned as a Python dictionary (dict).

.. code:: python

    results = myStats.compute()
    mean = results['mean']

The **mean**, **median** and **percentiles** are rounded to the 3rd decimal.
The standard deviation (**stddev**) is rounded to the 7th decimal.


Percentiles
-----------

The algorithm used to compute the percentiles is compatible with Numpy.
They give the same results over the same dataset.

| It uses a Linear Interpolation between adjacent ranks so the results might
  not be part of the dataset. This is different from the Near Rank algorithm
  where all the values are part of the dataset.
  See Wikipedia (Percentiles_) for details.

To access the value for a particular percentile, the characters 'th' should
be added to the value:

.. code:: python

    # retrieve the 10th and 50th percentiles
    x10 = results['10th']
    x50 = results['50th']


Changing the percentiles
........................

| The list of percentiles can be changed before invoking
  the ``compute`` function.
| The function ``percentiles`` takes a list of integer values that represents
  the new values to be calculated at the next call for compute.
| It will return the previous list of percentiles in case it has to be
  reinstated later.

.. code:: python

    new_list = [5, 15, 25, 35, 45]
    old_list = myStats.percentiles(new_list)

    results = myStats.compute()


Tests
-----

Run tests:

.. code:: bash

    $ tox

License
-------

This package is released under the Apache License 2.0. See the bundled
`LICENSE`_ file for details.





.. _Percentiles: https://en.wikipedia.org/wiki/Percentile#Second_variant,_%7F'%22%60UNIQ--postMath-00000047-QINU%60%22'%7F
.. _Numpy: https://numpy.org/
.. _LICENSE: https://github.com/aimktech/amtStats/blob/master/LICENSE.txt

.. |python| image:: https://img.shields.io/static/v1?label=python&message=3%2e7%2b&color=blue&style=flat-square
    :target: https://www.python.org
    :alt: Python 3.7+

.. |pypi| image:: https://img.shields.io/pypi/v/amtstats?color=blue&style=flat-square
    :target: https://pypi.org/project/amtstats
    :alt: Latest version released on PyPI

.. |build| image:: https://img.shields.io/travis/aimktech/amtStats/master.svg?style=flat-square
    :target: https://travis-ci.org/aimktech/amtStats
    :alt: Travis build

.. |coverage| image:: https://img.shields.io/coveralls/github/aimktech/amtStats/master?style=flat-square
    :alt: Tests coverage

.. |license| image:: https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square
    :target: https://raw.githubusercontent.com/aimktech/amtstats/master/LICENSE.txt
    :alt: Package license
