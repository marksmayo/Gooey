"""Script for setuptools."""
import sys
from setuptools import setup, find_packages


with open('README.md', encoding="utf-8") as readme:
    long_description = readme.read()

version = '1.2.0-ALPHA'

deps = [
    'Pillow>=4.3.0',
    'psutil>=5.4.2',
    'colored>=1.3.93',
    'pygtrie>=2.3.3',
    're-wx>=0.0.9',
    'typing-extensions==3.10.0.2',
    'wxpython>=4.1.0',
    "dataclasses>=0.8;python_version<'3.7'",
]

setup(
    name='Gooey',
    version=version,
    url='http://pypi.python.org/pypi/Gooey/',
    author='Chris Kiehl',
    author_email='audionautic@gmail.com',
    description=('Turn (almost) any command line program into a full GUI '
                 'application with one line'),
    license='MIT',
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=deps,
    include_package_data=True,
    dependency_links = ["http://www.wxpython.org/download.php"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Widget Sets',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    long_description='''

Gooey (Beta)
############


Turn (almost) any Python Console Program into a GUI application with one line
-----------------------------------------------------------------------------

.. image:: https://cloud.githubusercontent.com/assets/1408720/7904381/f54f97f6-07c5-11e5-9bcb-c3c102920769.png


Quick Start
-----------

Gooey is attached to your code via a simple decorator on your `main` method.

.. code-block::

  from gooey import Gooey
  @Gooey      <--- all it takes! :)
  def main():
      # rest of code



With the decorator attached, run your program and the GUI will now appear!

Checkout the full documentation, instructions, and source on `Github <https://github.com/chriskiehl/Gooey>`_'''
)
