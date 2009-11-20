from zope.component import queryMultiAdapter
from zope.app.event.objectevent import ObjectModifiedEvent
from zope.event import notify
from zope.interface import alsoProvides, directlyProvides, directlyProvidedBy
from eea.promotion.interfaces import IPromoted, IPromotion


class CreatePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        """Marks context as IPromoted

        Promotions that don't have an promo_imglink adapter are blocked from this action.
        This is because this adapter is required for their listing.
        """
        if queryMultiAdapter((self.context, self.request), name='imgview') == None:
            raise Exception, u"Sorry, no imgview adapter available for object at " + self.context.absolute_url()
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
            notify(ObjectModifiedEvent(self.context))
        promo.remove()
        directlyProvides(self.context, directlyProvidedBy(self.context) - IPromoted)
        self.context.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url())
