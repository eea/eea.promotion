""" Base
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
import eea.promotion


PRODUCTS = ['ATVocabularyManager', 'eea.vocab',]

PloneTestCase.installProduct('Products.NavigationManager')

@onsetup
def setup_promotion():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', eea.promotion)
    fiveconfigure.debug_mode = False

    PloneTestCase.installPackage('eea.themecentre')
    PloneTestCase.installPackage('p4a.video')

setup_promotion()
PloneTestCase.setupPloneSite(extension_profiles=('eea.promotion:default',))

class EEAPromotionTestCase(PloneTestCase.FunctionalTestCase):
    """ Test case class used for functional promotion tests. """
