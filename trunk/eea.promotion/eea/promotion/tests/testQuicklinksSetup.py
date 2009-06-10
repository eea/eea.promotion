from zope.interface import alsoProvides
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from eea.promotion.setuphandlers import setupQuicklinks
from eea.promotion.interfaces import IPromoted, IPromotion
from eea.promotion.catalog import FrontpageSectionIndex


PRODUCTS = ['RichTopic']


@onsetup
def setup_promotion():
    for i in PRODUCTS:
        PloneTestCase.installProduct(i)


setup_promotion()
PloneTestCase.setupPloneSite(products=PRODUCTS)


class Test(PloneTestCase.PloneTestCase):

    def afterSetUp(self):
        self.setRoles(['Manager'])
        portal = self.portal
        portal.invokeFactory('Folder', id='SITE')
        portal.SITE.invokeFactory('Folder', id='quicklinks')
        quicklinks = portal.SITE.quicklinks
        quicklinks.invokeFactory('Folder', id='spotlight')
        quicklinks.invokeFactory('Folder', id='multimedia')
        quicklinks.spotlight.invokeFactory('Document', id='testpromo')
        self.testpromo = quicklinks.spotlight.testpromo
        alsoProvides(self.testpromo, IPromoted)
        self.testpromo.locations = [u'Front Page']
        self.folders = quicklinks.listFolderContents()
        self.folders = [i for i in self.folders if i.portal_type == 'Folder']
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.setImportContext('profile-eea.promotion:default')
        setup_tool.runAllImportSteps()

    def testCriterion(self):
        portal = self.portal
        for i in self.folders:
            rt_id = '%s_internal_promotions' % i.id
            rt = getattr(i, rt_id)
            crit = rt.getCriterion('frontpage_section_ATSelectionCriterion')
            self.assertEquals(crit.value[0], u'/'.join(i.getPhysicalPath()))

    def testIndexAdapter(self):
        indexed_section = FrontpageSectionIndex(self.testpromo, None)()
        expected_section = IPromotion(self.testpromo).frontpage_section
        self.assertEquals(indexed_section, expected_section)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = makeSuite(Test)
    return  TestSuite(suite)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
