from zope.interface import implements
from zope.component import adapts
from interfaces import IPromoted, IPromotion
from zope.app.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict


KEY = 'eea.promotion'


class Promotion(object):
    implements(IPromotion)
    adapts(IPromoted)

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        mapping = annotations.get(KEY)
        if mapping is None:
            d = {'visibility': '', 'section': ''}
            mapping = annotations[KEY] = PersistentDict(d)
        self.mapping = mapping

    def section():
        def get(self):
            return self.mapping.get('section')
        def set(self, val):
            self.mapping['section'] = val
        return property(get, set)
    section = section()

    def visibility():
        def get(self):
            return self.mapping.get('visibility')
        def set(self, val):
            self.mapping['visibility'] = val
        return property(get, set)
    visibility = visibility()
