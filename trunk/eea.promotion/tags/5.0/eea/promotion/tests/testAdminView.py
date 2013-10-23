""" Test admin view
"""
from unittest import TestSuite
import doctest
from zope.interface import alsoProvides
from Testing.ZopeTestCase import FunctionalDocFileSuite
from eea.promotion.interfaces import IPromoted
from eea.promotion.promotion import Promotion
from eea.themecentre.interfaces import IThemeTagging
from eea.promotion.tests.base import EEAPromotionTestCase

optionflags =  (doctest.ELLIPSIS |
                doctest.NORMALIZE_WHITESPACE |
                doctest.REPORT_ONLY_FIRST_FAILURE)

class Test(EEAPromotionTestCase):
    """ Test
    """

    def afterSetUp(self):
        """ After setup
        """
        self.setRoles(['Manager'])
        portal = self.portal
        for i in range(0, 3):
            tid = 'test' + str(i)
            title = u'Test Item ' + str(i)
            item = portal[portal.invokeFactory('News Item',
                                               title=title,
                                               id=tid)]
            IThemeTagging(item).tags = [u'agriculture', u'air']
            alsoProvides(item, IPromoted)
            promo = Promotion(item)
            promo.locations = [u'Front Page', u'Themes']
            item.reindexObject()
            portal.portal_workflow.doActionFor(item, 'publish')

def test_suite():
    """ Test suite
    """
    suite = TestSuite((
        FunctionalDocFileSuite('admin.txt',
                     test_class=Test,
                     package='eea.promotion.browser',
                     optionflags=optionflags),
        ))
    return suite
