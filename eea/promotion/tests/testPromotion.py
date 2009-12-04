import unittest
from zope.testing import doctest
from zope.interface import implements
from zope.component import provideUtility, queryUtility
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName
from Testing.ZopeTestCase import FunctionalDocFileSuite
from base import EEAPromotionTestCase


class TestPromotion(EEAPromotionTestCase):

    def afterSetUp(self):
        from eea.promotion.interfaces import IPromotable
        from zope.interface import alsoProvides
        portal = self.portal
        self.setRoles(['Manager'])
        self.item = self.portal[portal.invokeFactory('News Item', id='test')]
        portal.portal_workflow.doActionFor(self.item, 'publish')
        alsoProvides(self.item, IPromotable)


class TestImageLink(EEAPromotionTestCase):

    def afterSetUp(self):
        import eea.promotion
        import os.path
        from zope.interface import alsoProvides
        from OFS.Image import Image
        from p4a.video.interfaces import IVideo, IVideoEnhanced
        portal = self.portal
        self.setRoles(['Manager'])

        id = portal.invokeFactory('News Item', id='test')
        self.item = portal[id]

        id = self.portal.invokeFactory('File', id='testfile')
        self.vid = portal[id]
        alsoProvides(self.vid, IVideoEnhanced)

        path = os.path.join(eea.promotion.__path__[0], 'tests', 'data', 'test.png')
        self.img_file = open(path, 'rb')
        IVideo(self.vid).video_image = Image('foobar', 'Foobar', self.img_file)


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
