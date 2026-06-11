import unittest

import setdoc

__all__ = ["test"]


@setdoc.basic
def test() -> unittest.TextTestResult:
    loader: unittest.TestLoader
    suite: unittest.TestSuite
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="keyalias.tests")
    return unittest.TextTestRunner().run(suite)
