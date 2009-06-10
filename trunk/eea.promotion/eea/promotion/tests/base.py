from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml


@onsetup
def setup_promotion():
    import eea.promotion
    zcml.load_config('configure.zcml', eea.promotion)

setup_promotion()
PloneTestCase.setupPloneSite()

class EEAPromotionTestCase(PloneTestCase.FunctionalTestCase):
    """ Test case class used for functional promotion tests. """
