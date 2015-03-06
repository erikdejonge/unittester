# coding=utf-8
"""
unittester
Active8 (05-03-15)
license: GNU-GPL2
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import int
from future import standard_library
standard_library.install_aliases()
from unittester import *
import unittest
def make_exception(s):
    """
    @type s: str, unicode
    @return: None
    """
    return int(s)


class SampleTestCase(unittest.TestCase):
    """
    @type unittest.TestCase: class
    @return: None
    """
    arguments = None

    def setUp(self):
        """
        setUp
        """
        self.myvar = "hello"

    def test_success(self):
        """
        test_assert_raises
        """
        self.assertIsNotNone(self.myvar)

    def test_exception(self):
        """
        test_exception
        """
        self.assertRaises(ValueError, make_exception, self.myvar)


class SampleTestCase2(unittest.TestCase):
    """
    @type unittest.TestCase: class
    @return: None
    """
    arguments = None

    def setUp(self):
        """
        setUp
        """
        self.myvar = 127

    def test_success(self):
        """
        test_assert_raises
        """
        self.assertIsNotNone(self.myvar)


def main():
    """
    main
    """
    unit_test_main(globals())


if __name__ == "__main__":
    main()
