#!/usr/bin/python

from distutils.core import Command
from unittest import TextTestRunner, TestLoader
from glob import glob
from os.path import splitext, basename, join as pjoin, walk
import os
import sys

def get_testfiles(cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    testfiles = []
    for t in glob(pjoin(cwd, 'tests', '*.py')):
        if not t.endswith('__init__.py'):
            testfiles.append('.'.join(
                ['tests', splitext(basename(t))[0]])
            )
    for t in glob(pjoin(cwd, 'test_*.py')):
        if not t.endswith('__init__.py'):
            testfiles.append(splitext(basename(t))[0])
    return testfiles

def run_tests(testfiles=None, cwd=None, verbosity=None):
    if testfiles is None:
        testfiles = get_testfiles(cwd=cwd)
    if verbosity is None:
        verbosity = 1
    tests = TestLoader().loadTestsFromNames(testfiles)
    t = TextTestRunner(verbosity=verbosity)
    t.run(tests)

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        '''
        Finds all the tests modules in tests/ and beginning with test_, and
        runs them.
        '''
        run_tests()

if __name__ == "__main__":
    verbosity = None
    if len(sys.argv) > 1:
        verbosity = int(sys.argv[1])
    run_tests(verbosity=verbosity)

