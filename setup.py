#!/usr/bin/python

"""An implementation of getopt (enhanced) written in python.

We use the getopt module and pipes.quote meaning we are very portable.
"""

from distutils.core import setup


# A list of classifiers can be found here:
#   http://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers = """\
Natural Language :: English
Development Status :: 4 - Beta
Environment :: Console
Topic :: Software Development :: User Interfaces
Topic :: System :: Shells
Topic :: Terminals
Topic :: Text Processing
Topic :: Utilities
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
License :: OSI Approved :: GNU General Public License (GPL)
Programming Language :: Python
Operating System :: OS Independent
"""

from sys import version_info

if version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(name='getopt-enhanced',
      description=doclines[0],
      long_description="\n".join(doclines[2:]),
      author='Gavin Beatty',
      author_email='gavinbeatty@gmail.com',
      maintainer='Gavin Beatty',
      maintainer_email='gavinbeatty@gmail.com',
      license = "http://www.gnu.org/licenses/gpl-3.0.txt",
      platforms=["any"],
      classifiers=filter(None, classifiers.split("\n")),
      url='http://code.google.com/p/getopt-enhanced/',
      version='1.1',
      scripts=['getopt-enhanced']
      )

