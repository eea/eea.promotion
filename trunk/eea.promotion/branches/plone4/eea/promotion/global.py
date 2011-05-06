""" Global
"""
from zope.interface import implements
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from p4a.video.interfaces import IVideoEnhanced
from eea.promotion.interfaces import IPromotion
from eea.promotion.interfaces import IGlobalPromotion


class GlobalPromotion(object):
    """ Global Promotion """
    implements(IGlobalPromotion)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.now = DateTime()

    def __call__(self):
        """Return first gloabl promotion found

        An image with id 'campaign-banner' has to be found.
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        result = catalog({
            'object_provides': 'eea.promotion.interfaces.IPromoted',
            'review_state': 'published',
            'effectiveRange' : self.now,
            'sort_on': 'effective',
            'sort_order' : 'reverse',
        })

        for brain in result:
            obj = brain.getObject()
            promo = IPromotion(obj)
            if promo.display_globally:
                return [{
                    'id' : brain.getId,
                    'Description' : brain.Description,
                    'Title' : brain.Title,
                    'url' : promo.url,
                    'absolute_url' : brain.getURL(),
                    'is_video' : IVideoEnhanced.providedBy(obj),
                }]
