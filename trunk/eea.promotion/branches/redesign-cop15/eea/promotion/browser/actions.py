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
        for obj in [self.context] + [i[0] for i in self.context.getTranslations().values()]:
            alsoProvides(obj, IPromoted) 
            notify(ObjectModifiedEvent(obj))
            obj.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url() + '/promotion_edit.html')


class RemovePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        for obj in [self.context] + [i[0] for i in self.context.getTranslations().values()]:
            if IPromoted.providedBy(obj):
                promo = IPromotion(obj)
                if promo.display_on_frontpage:
                    notify(ObjectModifiedEvent(obj))
                promo.remove()
                directlyProvides(obj, directlyProvidedBy(obj) - IPromoted)
                obj.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url() + '/edit?portal_status_message=Promotions removed from item and its translations')


class PromoteTranslations(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        for trans in self.context.getTranslations().values():
            obj = trans[0]
            if not IPromoted.providedBy(obj):
                alsoProvides(obj, IPromoted) 
                notify(ObjectModifiedEvent(obj))
                obj.reindexObject()
        return self.request.RESPONSE.redirect(self.context.absolute_url() + '/edit?portal_status_message=Translations was promoted')
