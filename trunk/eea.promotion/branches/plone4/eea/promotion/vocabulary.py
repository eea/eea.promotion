""" Vocabulary
"""
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.app.schema.vocabulary import IVocabularyFactory


ALLOWED_LOCATIONS = [u'Front Page', u'Themes', u'Global']

class LocationsVocabulary(object):
    """ Locations Vocabulary """
    implements(IVocabularyFactory)

    def __call__(self, context):
        return SimpleVocabulary.fromValues(ALLOWED_LOCATIONS)

LocationsVocabularyFactory = LocationsVocabulary()
