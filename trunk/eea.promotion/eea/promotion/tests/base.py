from Testing import ZopeTestCase
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure

dependencies = []

@onsetup
def setup_promotion():
    fiveconfigure.debug_mode = True
    import Products.Five
    import eea.promotion
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', eea.promotion)
    fiveconfigure.debug_mode = False
    PloneTestCase.installProduct('Five')

setup_promotion()
PloneTestCase.setupPloneSite()

class EEAPromotionTestCase(PloneTestCase.FunctionalTestCase):
    """ Test case class used for functional promotion tests. """
