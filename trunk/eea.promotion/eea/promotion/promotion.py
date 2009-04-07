from zope.interface import implements
from interfaces import IPromotedItem
from zope.app.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict


KEY = 'eea.promotion'


class PromotedItem(object):
    implements(IPromotedItem)

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context)
        mapping = annotation.get(KEY)
        if mapping is None:
            d = {'visibility': '', 'location': ''}
            mapping = annotation[KEY] = PersistentDict(d)
        self.mapping = mapping

    def location():
        def get(self):
            return self.mapping.get('location')
        def set(self, val):
            self.mapping['location'] = val
        return property(get, set)
    location = location()

    def visibility():
        def get(self):
            return self.maping.get('visibility')
        def set(self, val):
            self.mapping['visibility'] = val
        return property(get, set)
    visibility = visibility()
