def setupManagePage(context):
    # Removed due to new admin view. See #2469
    pass


def setupQuicklinks(context):
    """Set up the quicklink folders so that they also list internal promotions.

    To do this, we add a RichTopic in every quicklinks sub-folder.
    """
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a 
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    
    if context.readDataFile('eea.promotion_various.txt') is None:
        return

    portal = context.getSite()

    # If portal/SITE does not exist, we're probably in some unrelated test
    # environment:
    if not hasattr(portal, 'SITE'):
        return

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
    result = catalog.searchResults({'portal_type': 'Promotion', 'Language': 'all'})
    for i in result:
        i.getObject().reindexObject()
    result = catalog.searchResults({'object_provides': 'eea.promotion.interfaces.IPromoted', 'Language': 'all'})
    for i in result:
        i.getObject().reindexObject()


def addOurRoles(context):
   """Add our extra roles to Plone.

   Part of this is done through GenericSetup, but adding roles to the
   PlonePAS role manager does not work there.

   Note: in Plone 3.0 (beta) this function is not needed, in Plone
   2.5 it is.
   """
   portal = context.getSite()
   role_manager = portal.acl_users.portal_role_manager
   pas_roles = role_manager.listRoleIds()
   role = 'PromotionManager'
   if role not in pas_roles:
       role_manager.addRole(role)

