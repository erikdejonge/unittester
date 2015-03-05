# coding=utf-8
"""
unittester
erik@a8.nl (05-03-15)
license: GNU-GPL2
"""
from unittester import *


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
