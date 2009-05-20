def setupManagePage(context):
    portal = context.getSite()
    if not hasattr(portal.SITE.cms, 'promotion_manage'):
        portal.SITE.cms.invokeFactory('RichTopic', id='promotion_manage')
        promotion_manage = portal.SITE.cms['promotion_manage']
        promotion_manage.setTitle(u'Manage Promotions')
        crit = promotion_manage.addCriterion('object_provides', 'ATSelectionCriterion')
        crit.setValue('eea.promotion.interfaces.IPromoted')


def setupQuicklinks(context, portal=None):
    """Set up the quicklink folders so that they also list internal promotions.

    To do this, we add a RichTopic in every quicklinks sub-folder.
    """
    portal = portal or context.getSite()

    # The quicklinks subfolders get their locally allowed types by aquisition,
    # that is from quicklinks.
    quicklinks = portal.SITE.quicklinks
    allowed = list(quicklinks.getLocallyAllowedTypes())
    if not 'RichTopic' in allowed:
        allowed.append('RichTopic')
    quicklinks.setLocallyAllowedTypes(allowed)

    folders = [i for i in quicklinks.listFolderContents() if (i != quicklinks) and (i.portal_type == 'Folder')]
    for i in  folders:
        id = '%s_internal_promotions' % i.id
        if hasattr(i, id):
            i.manage_delObjects(id)

        i.invokeFactory('RichTopic', id=id)
        rt = getattr(i, id)
        rt.selectViewTemplate('folder_summary_view')
        rt.setTitle(i.Title())
        i.setDefaultPage(rt.getId())
        portal.portal_workflow.doActionFor(rt, 'publish')

        c = rt.addCriterion('frontpage_section', 'ATSelectionCriterion')
        c.setValue(u'/'.join(i.getPhysicalPath()))

    catalog = portal.portal_catalog
    result = catalog.searchResults({'portal_type': 'Promotion'})
    for i in result:
        i.getObject().reindexObject()
