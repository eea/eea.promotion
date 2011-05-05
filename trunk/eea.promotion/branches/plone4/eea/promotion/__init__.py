from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore import utils
from Globals import package_home
from os.path import dirname
from AccessControl import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

GLOBALS = globals()

ppath = utils.ProductsPath
utils.ProductsPath.append(dirname(package_home(GLOBALS)))
registerDirectory('skins', GLOBALS)
utils.ProductsPath = ppath

security = ModuleSecurityInfo('eea.promotions')
security.declarePublic('ManagePromotions')
ManagePromotions = 'Manage promotions'
setDefaultRoles(ManagePromotions, ('Manager',))
