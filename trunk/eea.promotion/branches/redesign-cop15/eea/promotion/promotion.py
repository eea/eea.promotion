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
            d = {'locations': [],
                 'frontpage_section': u'',
                 'themepage_section': None,
                 'themes': []}
            mapping = annotations[KEY] = PersistentDict(d)
        self.mapping = mapping
        self.is_external = False
        self.url = context.absolute_url()

    def remove(self):
        annotations = IAnnotations(self.context)
        del annotations[KEY]

    def locations():
        def get(self):
            return self.mapping.get('locations')
        def set(self, val):
            self.mapping['locations'] = val
        return property(get, set)
    locations = locations()

    def themepage_section():
        def get(self):
            return self.mapping.get('themepage_section')
        def set(self, val):
            self.mapping['themepage_section'] = val
        return property(get, set)
    themepage_section = themepage_section()

    def frontpage_section():
        def get(self):
            return self.mapping.get('frontpage_section')
        def set(self, val):
            self.mapping['frontpage_section'] = val
        return property(get, set)
    frontpage_section = frontpage_section()

    @property
    def active(self):
        return len(self.locations) > 0

    @property
    def display_on_frontpage(self):
        return u'Front Page' in self.locations

    @property
    def display_on_themepage(self):
        return u'Themes' in self.locations

    @property
    def display_globally(self):
        if not (u'Global' in self.locations):
            return False
        if self.frontpage_section.split('/')[-1] == 'spotlight':
            return True
        return False

    def themes():
        def get(self):
            return self.mapping.get('themes')
        def set(self, val):
            self.mapping['themes'] = val
        return property(get, set)
    themes = themes()

    @property
    def edit_url(self):
        return self.context.absolute_url() + '/promotion_edit.html'
