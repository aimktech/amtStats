#!/usr/bin/env python
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# retrieve long description
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as fh:
    README = fh.read()

# retrieve package version
with open(os.path.join(here, 'amtStats', '__init__.py')) as fh:
    for line in fh:
        if '__version__' in line:
            VERSION=eval(line.split('=')[1].strip(' \r\n'))
            break

# setup
setup(
    name='amtStats',
    version=VERSION,
    description='Simple statistics module',
    long_description=README,
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='',
    author='aimktech',
    author_email='code@aimechanics.tech',
    url='https://github.com/aimktech/amtStats',
    license='Apache 2.0',
    packages=find_packages(exclude=["docs", "tests"]),
    package_data={"amtStats": ["py.typed"]},
    platforms=["any"],
    zip_safe=False,
)