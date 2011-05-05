""" eea.promotion package """

from Products.CMFCore.permissions import setDefaultRoles
from AccessControl import ModuleSecurityInfo

security = ModuleSecurityInfo('eea.promotions')
security.declarePublic('ManagePromotions')
ManagePromotions = 'Manage promotions'
setDefaultRoles(ManagePromotions, ('Manager',))
