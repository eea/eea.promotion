def setupManagePage(context):
    portal = context.getSite()
    if not hasattr(portal.SITE.cms, 'promotion_manage'):
        portal.SITE.cms.invokeFactory('RichTopic', id='promotion_manage')
        promotion_manage = portal.SITE.cms['promotion_manage']
        promotion_manage.setTitle(u'Manage Promotions')
        crit = promotion_manage.addCriterion('object_provides', 'ATSelectionCriterion')
        crit.setValue('eea.promotion.interfaces.IPromoted')
