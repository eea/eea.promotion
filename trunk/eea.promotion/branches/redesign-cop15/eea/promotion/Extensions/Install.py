import transaction
from Products.CMFCore.utils import getToolByName


PROFILE = 'eea.promotion:default'
PRODUCTS = 'RichTopic'


def install(self, reinstall=False):
    portal_setup = getToolByName(self, 'portal_setup')
    portal_setup.setImportContext('profile-%s' % PROFILE)
    portal_setup.runAllImportSteps()
    product_name = PROFILE.split(':')[0]
    qi = getToolByName(self, 'portal_quickinstaller')
    qi.notifyInstalled(product_name)
