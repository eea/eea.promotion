from zope.interface import implements
from zope.component import adapts
from interfaces import IPromoted, IPromotion
from zope.app.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict
from eea.themecentre.interfaces import IThemeTagging
from Products.NavigationManager.sections import INavigationSectionPosition


KEY = 'eea.promotion'


class Promotion(object):
    implements(IPromotion)
    adapts(IPromoted)

    def __init__(self, context):
        self.context = context
        annotations = IAnnotations(context.getCanonical())
        mapping = annotations.get(KEY)
        if mapping is None:
            mapping = annotations[KEY] = PersistentDict({'locations': []})
        self.mapping = mapping
        self.is_external = False
        self.url = context.absolute_url()

    def remove(self):
        annotations = IAnnotations(self.context.getCanonical())
        del annotations[KEY]

    def locations():
        def get(self):
            return self.mapping.get('locations')
        def set(self, val):
            self.mapping['locations'] = val
        return property(get, set)
    locations = locations()

    @property
    def themepage_section(self):
        return INavigationSectionPosition(self.context).section

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
        if u'Global' in self.locations:
            return True
        return False

    @property
    def themes(self):
        return IThemeTagging(self.context).tags

    @property
    def edit_url(self):
        return self.context.absolute_url() + '/promotion_edit.html'
