""" Test promotion
"""
from unittest import TestSuite
import os.path
import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite
from eea.promotion.tests.base import EEAPromotionTestCase
import eea.promotion
from eea.promotion.interfaces import IPromotable
from zope.interface import alsoProvides

optionflags =  (doctest.ELLIPSIS |
                doctest.NORMALIZE_WHITESPACE |
                doctest.REPORT_ONLY_FIRST_FAILURE)

class TestPromotion(EEAPromotionTestCase):
    """ Test promotion
    """

    def afterSetUp(self):
        """ After setup
        """
        portal = self.portal
        self.setRoles(['Manager'])
        self.item = self.portal[portal.invokeFactory('News Item', id='test')]
        portal.portal_workflow.doActionFor(self.item, 'publish')
        alsoProvides(self.item, IPromotable)

        path = os.path.join(eea.promotion.__path__[0],
                            'tests',
                            'data',
                            'test.png')
        self.img = open(path, 'rb').read()

def test_suite():
    """ Test suite
    """
    suite = TestSuite((
        FunctionalDocFileSuite('promotion.txt',
                     test_class=TestPromotion,
                     package = 'eea.promotion.tests',
                     optionflags=optionflags),
        FunctionalDocFileSuite('bugs.txt',
                     test_class=TestPromotion,
                     package = 'eea.promotion.tests',
                     optionflags=optionflags),
        ))
    return suite
