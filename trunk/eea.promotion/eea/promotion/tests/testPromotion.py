import unittest
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite
from base import EEAPromotionTestCase


class Test(EEAPromotionTestCase):

    def afterSetup(self):
        pass


def test_suite():
    suite = unittest.TestSuite((
        FunctionalDocFileSuite('promotion.txt',
                     test_class=Test,
                     package = 'eea.promotion.tests',
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS|doctest.REPORT_ONLY_FIRST_FAILURE
                     ),
        ))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
