""" Admin
"""
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, noLongerProvides
from eea.promotion.interfaces import IPromotion, IPromoted
from eea.promotion.browser.interfaces import IAdminView
from DateTime.DateTime import DateTime


class AdminView(BrowserView):
    """ Admin view
    """
    implements(IAdminView)
    template = ViewPageTemplateFile('admin.pt')


    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request

    def current_promotions(self):
        """ return the brains with promotions from site
        """
        now = DateTime()
        catalog = getToolByName(self.context, 'portal_catalog')
        result = catalog({
            'object_provides': [
               'eea.promotion.interfaces.IPromoted',
               'Products.EEAContentTypes.content.interfaces.IExternalPromotion',
            ],
            'review_state': 'published',
            'effectiveRange': now,
            })
        return result

    def find_promotions(self):
        """ Find promotions
        """
        ret = []
        result = self.current_promotions()
        for brain in result:
            obj = brain.getObject()
            try:
                promo = IPromotion(obj)
            except Exception:
                continue
            ret.append({
                'title': brain.Title,
                'href': promo.edit_url,
                'locations': u', '.join(promo.locations),
                'themes': u', '.join(promo.themes),
                'themepage_section':
                        (promo.themepage_section or '').split('/')[-1],
                'url' : promo.url,
                'absolute_url' : brain.getURL(),
                'active': promo.active,
                'is_external': promo.is_external,
            })
        return ret

    def disable_inactive_promotions(self):
        """ Disable all inactive promotions
        """
        result = self.current_promotions()
        for brain in result:
            obj = brain.getObject()
            try:
                promo = IPromotion(obj)
            except Exception:
                continue
            if not promo.active:
                noLongerProvides(obj, IPromoted)
                obj.reindexObject(idxs=['object_provides'])
        msg = "Inactive Promotions have been succesfully disabled"
        IStatusMessage(self.request).addStatusMessage(msg, type='info')
        return self.request.response.redirect(self.context.absolute_url() +
                                              '/@@promotion_admin_view')

    def __call__(self):
        if "submit" not in self.request.form:
            return self.template()
        return self.disable_inactive_promotions()
