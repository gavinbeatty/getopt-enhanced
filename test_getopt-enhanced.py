#!/usr/bin/python

#/***************************************************************************
# *   Copyright (C) 2010 by Gavin Beatty                                    *
# *   gavinbeatty@gmail.com                                                 *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU General Public License for more details.                          *
# *                                                                         *
# *   You should have received a copy of the GNU General Public License     *
# *   along with this program; if not, write to the                         *
# *   Free Software Foundation, Inc.,                                       *
# *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
# ***************************************************************************/


try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import unittest
import subprocess as sp

class ModTests(unittest.TestCase):
    def setUp(self):
        self.stdout = None
        self.stderr = None

    def _argv(self, args):
        return ['./getopt-enhanced'] + args

    def _main(self, args):
        proc = sp.Popen(self._argv(args), stdout=sp.PIPE, stderr=sp.PIPE
            , universal_newlines=True)
        self.stdout, self.stderr = proc.communicate()
        return proc.returncode

    def _test(self, args, retcode, output=None, errput=None):
        self.assertEqual(self._main(args), retcode)
        if output is not None:
            self.assertEqual(self.stdout, output+'\n')
        if errput is not None:
            self.assertEqual(self.stdout, errput+'\n')

    def _fail(self, args, output=None, errput=None):
        self.assertNotEqual(self._main(args), 0)
        if output is not None:
            self.assertEqual(self.stdout, output+'\n')
        if errput is not None:
            self.assertEqual(self.stdout, errput+'\n')

    def testNone(self):
        self._test([], 0, output=' --')
        self._test(['--'], 0, output=' --')
        self._test(['-o', 'h'], 0, output=' --')
        self._test(['-o', 'h', '--'], 0, output=' --')
        self._test(['-l', 'help'], 0, output=' --')
        self._test(['-l', 'help', '--'], 0, output=' --')
        self._test(['-o', 'h', '-l', 'help'], 0, output=' --')
        self._test(['-o', 'h', '-l', 'help', '--'], 0, output=' --')

    def testEmpty(self):
        self._test([''], 0, output=" -- ''")
        self._test(['--', ''], 0, output=" -- ''")
        self._test(['-o', 'h', ''], 0, output=" -- ''")
        self._test(['-o', 'h', '--', ''], 0, output=" -- ''")
        self._test(['-l', 'help', ''], 0, output=" -- ''")
        self._test(['-l', 'help', '--', ''], 0, output=" -- ''")
        self._test(['-o', 'h', '-l', 'help', ''], 0, output=" -- ''")
        self._test(['-o', 'h', '-l', 'help', '--', ''], 0, output=" -- ''")
        self._test(['-o', 'hab:c', '-l', 'help,arg:,none,arg2:', ''], 0, output=" -- ''")
        self._test(['-o', 'h', '-l', 'help', '--', ''], 0, output=" -- ''")

    def testNormal(self):
        self._test(['-o', 'hab:c', '--', '-a', '-b', '-c', '-h', 'arg', '-c'
            , '--', '-h', 'litarg']
            , 0
            , output=' -a -b -c -h -c -- arg -h litarg')
        self._test(['-o', 'hab:c', '--', '-a', '-b', '-c', '-h', 'sp aced'
            , '-c', '--', '-h', "quote'arg$me"]
            , 0
            , output=" -a -b -c -h -c -- 'sp aced' -h \"quote'arg\\$me\"")

if __name__ == '__main__':
    unittest.main()

