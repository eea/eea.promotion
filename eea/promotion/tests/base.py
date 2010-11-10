from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure


PRODUCTS = ['ATVocabularyManager', 'PloneLanguageTool', 'FiveSite', 'eea.vocab', 'eea.promotion']


@onsetup
def setup_promotion():
    fiveconfigure.debug_mode = True
    import Products.Five
    import Products.FiveSite
    import eea.promotion
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.FiveSite)
    zcml.load_config('configure.zcml', eea.promotion)
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    for product in PRODUCTS:
        PloneTestCase.installProduct(product)

setup_promotion()
PloneTestCase.setupPloneSite(products=PRODUCTS)

class EEAPromotionTestCase(PloneTestCase.FunctionalTestCase):
    """ Test case class used for functional promotion tests. """
