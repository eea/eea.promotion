from zope.interface import alsoProvides, directlyProvides, directlyProvidedBy
from eea.promotion.interfaces import IPromotedItem


class CreatePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        alsoProvides(self.context, IPromotedItem) 
        return self.request.RESPONSE.redirect(self.context.absolute_url() + '/promotion_edit.html')


class RemovePromotion(object):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        directlyProvides(self.context, directlyProvidedBy(self.context) - IPromotedItem)
        return self.request.RESPONSE.redirect(self.context.absolute_url())
