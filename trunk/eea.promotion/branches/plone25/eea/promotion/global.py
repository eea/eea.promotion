from zope.component import getMultiAdapter
from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from interfaces import IPromotion


class GlobalPromotion(object):
    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.now = DateTime()

    def global_promotion(self):
        """ """
        catalog = getToolByName(self.context, 'portal_catalog')
        query = {'object_provides': 'eea.promotion.interfaces.IPromoted',
                 'review_state': 'published',
                 'effectiveRange' : self.now}
        result = catalog.searchResults(query)
        for t in result:
            obj = t.getObject()
            promo = IPromotion(obj)
            if promo.display_globally:
                info = {'id' : t.getId,
                        'Description' : t.Description,
                        'Title' : t.Title,
                        'url' : promo.url,
                        'style' : 'display: none;',
                        'imglink' : getMultiAdapter((obj, obj.REQUEST),
                             name='promo_imglink')('thumb'),
                        'image' : t.getURL() + '/image' }
                return [info]
