from zope.component import getMultiAdapter
from zope.interface import implements
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from eea.promotion.interfaces import IPromoted, IPromotion
from eea.promotion.browser.interfaces import IAdminView


class AdminView(BrowserView):
    implements(IAdminView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def find_promotions(self):
        ret = []
        catalog = self.context.portal_catalog
        query = {'object_provides': 'eea.promotion.interfaces.IPromoted',
                'review_state': 'published'}
        result = catalog.searchResults(query)
        for i in result:
            obj = i.getObject()
            promo = IPromotion(obj)
            info = {'title': i.Title,
                    'href': obj.absolute_url() + '/promotion_edit.html',
                    'locations': u', '.join(promo.locations), 
                    'themes': u', '.join(promo.themes),
                    'frontpage_section': (promo.frontpage_section or '').split('/')[-1],
                    'imgtag' : getMultiAdapter((obj, obj.REQUEST), name='imgtag'),
                    'active': promo.active}
            ret.append(info)
        return ret

    __call__ = ViewPageTemplateFile('admin.pt')
