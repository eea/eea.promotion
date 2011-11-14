from zope.interface import implements
from zope.component import adapts
from eea.promotion.interfaces import IFrontpageSectionIndex
from eea.promotion.interfaces import IPromoted, IPromotion


class FrontpageSectionIndex(object):
    """ """
    implements(IFrontpageSectionIndex)

    def __init__(self, context, request):
        """ """
        self.context = context

    def __call__(self):
        """ """
        promo = IPromotion(self.context)
        if promo.display_on_frontpage:
            return promo.frontpage_section
        return u''
