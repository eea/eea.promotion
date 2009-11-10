from zope.component import getMultiAdapter
from zope.interface import implements
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from eea.promotion.interfaces import IPromoted, IPromotion
from eea.promotion.browser.interfaces import IAdminView
from DateTime.DateTime import DateTime


class AdminView(BrowserView):
    implements(IAdminView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def find_promotions(self):
        ret = []
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
        for brain in result:
            obj = brain.getObject()
            try:
                promo = IPromotion(obj)
            except:
                continue
            ret.append({
                'title': brain.Title,
                'href': promo.edit_url,
                'locations': u', '.join(promo.locations), 
                'themes': u', '.join(promo.themes),
                'themepage_section': (promo.themepage_section or '').split('/')[-1],
                'imgtag': getMultiAdapter((obj, obj.REQUEST), name='imgtag'),
                'active': promo.active,
                'is_external': promo.is_external,
            })
        return ret

    __call__ = ViewPageTemplateFile('admin.pt')
