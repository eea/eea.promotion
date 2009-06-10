import unittest
from zope.testing import doctest
from zope.interface import implements
from zope.component import provideUtility
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from Testing.ZopeTestCase import FunctionalDocFileSuite
from base import EEAPromotionTestCase


class ThemesVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(['Snow', 'Space', 'Sand'])


class FrontPageSectionsVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        sections = {'Spotlight': '/plone/SITE/quicklinks/spotlight'}
        return SimpleVocabulary.fromItems(sections.items())


class ThemepageSectionsVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues([u'Left', u'Center', u'Right'])


class Test(EEAPromotionTestCase):

    def afterSetUp(self):
        provideUtility(ThemesVocabulary(), name=u'Allowed themes')
        provideUtility(ThemepageSectionsVocabulary(), name=u'Themepage Promotion Sections')
        provideUtility(FrontPageSectionsVocabulary(), name=u'Frontpage Promotion Sections')


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
