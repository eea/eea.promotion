from zope.interface import implements
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


ALLOWED_LOCATIONS = ['Front Page', 'Highlights', 'Whole Site']

VISIBILITY_LEVELS = {'Invisible': 1,
                     'Low': 2,
                     'Medium': 3,
                     'High': 4,
                     'Global': 5}


class LocationVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_LOCATIONS)


class VisibilityVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromItems(VISIBILITY_LEVELS.items())


LocationVocabularyFactory = LocationVocabulary()
VisibilityVocabularyFactory = VisibilityVocabulary()
