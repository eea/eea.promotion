import unittest
import doctest
from zope.interface import alsoProvides
from Testing.ZopeTestCase import FunctionalDocFileSuite
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from eea.promotion.setuphandlers import setupQuicklinks
from eea.promotion.interfaces import IPromoted, IPromotion
from eea.promotion.promotion import Promotion
from eea.themecentre.interfaces import IThemeTagging
from eea.promotion.tests.base import EEAPromotionTestCase


PloneTestCase.setupPloneSite()


class Test(EEAPromotionTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])
        portal = self.portal
        for i in range(0, 3):
            id = 'test' + str(i)
            title = u'Test Item ' + str(i)
            item = portal[portal.invokeFactory('News Item', title=title, id=id)]
            IThemeTagging(item).tags = [u'agriculture', u'air']
            alsoProvides(item, IPromoted)
            promo = Promotion(item)
            promo.locations = [u'Front Page', u'Themes']
            item.reindexObject()
            portal.portal_workflow.doActionFor(item, 'publish')


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = unittest.TestSuite((
        FunctionalDocFileSuite('admin.txt',
                     test_class=Test,
                     package='eea.promotion.browser',
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS|doctest.REPORT_ONLY_FIRST_FAILURE
                     ),
        ))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
