import unittest
import os.path
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite
from base import EEAPromotionTestCase
import eea.promotion


class TestPromotion(EEAPromotionTestCase):

    def afterSetUp(self):
        from eea.promotion.interfaces import IPromotable
        from zope.interface import alsoProvides
        portal = self.portal
        self.setRoles(['Manager'])
        self.item = self.portal[portal.invokeFactory('News Item', id='test')]
        portal.portal_workflow.doActionFor(self.item, 'publish')
        alsoProvides(self.item, IPromotable)

        path = os.path.join(eea.promotion.__path__[0], 'tests', 'data', 'test.png')
        self.img = open(path, 'rb').read()


def test_suite():
    suite = unittest.TestSuite((
        FunctionalDocFileSuite('promotion.txt',
                     test_class=TestPromotion,
                     package = 'eea.promotion.tests',
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS|doctest.REPORT_ONLY_FIRST_FAILURE
                     ),
        FunctionalDocFileSuite('bugs.txt',
                     test_class=TestPromotion,
                     package = 'eea.promotion.tests',
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS|doctest.REPORT_ONLY_FIRST_FAILURE
                     ),
        ))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
