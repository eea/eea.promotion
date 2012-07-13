""" Promotion
"""
from zope.interface import implements
from zope.component import adapts
from eea.promotion.interfaces import IPromoted, IPromotion
from zope.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict
from eea.themecentre.interfaces import IThemeTagging
from Products.CMFPlone.utils import isDefaultPage, parent
from Products.NavigationManager.interfaces import INavigationSectionPosition

KEY = 'eea.promotion'

class Promotion(object):
    """ Promotion
    """
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
        if isDefaultPage(context, context.REQUEST):
            self.url = parent(context).absolute_url()
        else:
            self.url = context.absolute_url()

    def remove(self):
        """ Remove
        """
        annotations = IAnnotations(self.context.getCanonical())
        del annotations[KEY]

    def getl(self):
        """ Get location
        """
        return self.mapping.get('locations')

    def setl(self, val):
        """ Set location
        """
        self.mapping['locations'] = val

    locations = property(getl, setl)

    @property
    def themepage_section(self):
        """ Theme section
        """
        return INavigationSectionPosition(self.context).section

    @property
    def active(self):
        """ Active
        """
        return len(self.locations) > 0

    @property
    def display_on_frontpage(self):
        """ Display on frontpage
        """
        return u'Front Page' in self.locations

    @property
    def display_on_themepage(self):
        """ Display on themepage
        """
        return u'Themes' in self.locations

    @property
    def display_globally(self):
        """ Display globally
        """
        return u'Global' in self.locations

    @property
    def display_in_spotlight(self):
        """ Display in spotlight
        """
        return u'Spotlight' in self.locations

    @property
    def display_on_datacentre(self):
        """ Display in datacentre
        """
        return u'Datacentre' in self.locations

    @property
    def themes(self):
        """ Themes
        """
        return IThemeTagging(self.context).tags

    @property
    def edit_url(self):
        """ Edit URL
        """
        return self.context.absolute_url() + '/promotion_edit.html'
