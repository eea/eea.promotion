from zope.interface import implements
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


ALLOWED_LOCATIONS = [u'Front Page', u'Themes', u'Global']
ALLOWED_FRONT_PAGE_SECTIONS = [u'Spotlight', u'Center']
ALLOWED_THEME_PAGE_SECTIONS = [u'Left', u'Right', u'Center']
ALLOWED_THEMES = [u'Climate Change', u'Environment', u'Ice Cream']


class LocationsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_LOCATIONS)


class FrontPageSectionsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_FRONT_PAGE_SECTIONS)


class ThemePageSectionsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_THEME_PAGE_SECTIONS)


class ThemesVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_THEMES)


FrontPageSectionsVocabularyFactory = FrontPageSectionsVocabulary()
ThemePageSectionsVocabularyFactory = ThemePageSectionsVocabulary()
LocationsVocabularyFactory = LocationsVocabulary()
ThemesVocabularyFactory = ThemesVocabulary()
