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
    
    # Not using quicklink folders anymore. See #2728
    pass


def addOurRoles(context):
    """Add our extra roles to Plone.

    Part of this is done through GenericSetup, but adding roles to the
    PlonePAS role manager does not work there.

    Note: in Plone 3.0 (beta) this function is not needed, in Plone
    2.5 it is.
    """
    # only run this step if we are in eea.design profile
    if context.readDataFile('eea.promotion_various.txt') is None:
        return

    portal = context.getSite()
    role_manager = portal.acl_users.portal_role_manager
    pas_roles = role_manager.listRoleIds()
    role = 'PromotionManager'
    if role not in pas_roles:
        role_manager.addRole(role)

