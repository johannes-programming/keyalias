import unittest
from typing import *

__all__ = ["test"]


def test() -> unittest.TextTestResult:
    loader: unittest.TestLoader
    suite: unittest.TestSuite
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="keyalias.tests")
    return unittest.TextTestRunner().run(suite)
