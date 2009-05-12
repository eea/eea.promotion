from zope.app.event.objectevent import ObjectModifiedEvent
from zope.event import notify
from zope.interface import alsoProvides, directlyProvides, directlyProvidedBy
from eea.promotion.interfaces import IPromoted, IPromotion
from Products.EEAContentTypes.cache import invalidateFrontpageMethodCache


class CreatePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        alsoProvides(self.context, IPromoted) 
        notify(ObjectModifiedEvent(self.context))
        self.context.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url() + '/promotion_edit.html')


class RemovePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        promo = IPromotion(self.context)
        if promo.display_on_frontpage:
            invalidateFrontpageMethodCache(self.context, None)
        promo.remove()
        directlyProvides(self.context, directlyProvidedBy(self.context) - IPromoted)
        self.context.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url())
