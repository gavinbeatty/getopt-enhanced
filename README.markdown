getopt-enhanced
===============
Gavin Beatty <gavinbeatty@gmail.com>

getopt-enhanced: an implementation of getopt (enhanced) written in python. We
use the getopt module and pipes.quote meaning we are very portable.

    Usage: getopt-enhanced.py [OPTIONS] [-- ARGUMENTS]

For more usage details, see the manual.


Dependencies
------------

Everything is written using only fully cross-platform python.


License
-------

getopt-enhanced Copyright 2009, 2010 Gavin Beatty <gavinbeatty@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You can find the GNU General Public License at:
http://www.gnu.org/licenses/


Install
-------

Use setuptools in the usual way:
    sudo python setup.py install

To install only for the current user:
    python setup.py install --user

For additional help:
    python setup.py --help


Install documentation
---------------------

Default installation prefix is /usr/local

    sudo make install-docs

Install to your own prefix:

    make install-docs prefix=~/.local


Website
-------
http://code.google.com/p/getopt-enhanced/


