"""
This module contains parts from Products.EEAContentTypes that we need for our
test environment.

The code below was copied from Products.EEAContentTypes.setup. This is because
Five loads all products available, which includes eea.themecentre. This causes
the 'Allowed Themes' vocabulary from eea.themecentre to be loaded, but the
ATVocabulary it gets its values from is not. Therefore we do it manually. This
avoids a dependency on the heavy EEAContentTypes product.
"""
from Products.CMFCore.utils import getToolByName


vocabs = {}

vocabs['themes'] = (
    ('default', 'Default'),
    ('acidification', 'Acidification'),
    ('agriculture', 'Agriculture'),
    ('air', 'Air'),
    ('air_quality', 'Air quality'),
    ('biodiversity', 'Biodiversity change'),
    ('chemicals', 'Chemicals'),
    ('climate', 'Climate change'),
    ('coasts_seas', 'Coasts and seas'),
    ('energy', 'Energy'),
    ('env_information', 'Environmental information'),
    ('env_management', 'Environmental management and practices'),
    ('env_reporting', 'Environmental reporting'),
    ('env_scenarios', 'Environmental scenarios'),
    ('fisheries', 'Fisheries'),
    ('households', 'Households'),
    ('human_health', 'Human health'),
    ('industry', 'Industry'),
    ('natural_resources', 'Natural resources'),
    ('nature', 'Nature'),
    ('noise', 'Noise'),
    ('ozone', 'Ozone depletion'),
    ('policy', 'Policy analysis'),
    ('population', 'Population amd economy'),
    ('regions', 'Regions'),
    ('soil', 'Soil'),
    ('tourism', 'Tourism'),
    ('transport', 'Transport'),
    ('urban', 'Urban environment'),
    ('various', 'Various other issues'),
    ('waste', 'Waste'),
    ('water', 'Water'),
)

def setupATVocabularies(portal):
    """ Installs all AT-based Vocabularies """
    
    from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
    
    vkeys = vocabs.keys()
    atvm = getToolByName(portal, ATVOCABULARYTOOL, None)
    if atvm is None:
        return
    
    for vkey in vkeys:

        print "adding vocabulary %s" % vkey
        
        if hasattr(atvm, vkey):
            continue
        
        atvm.invokeFactory('SimpleVocabulary', vkey)
        vocab = atvm[vkey]
        for (ikey, value) in vocabs[vkey]:
            vocab.invokeFactory('SimpleVocabularyTerm', ikey)
            vocab[ikey].setTitle(value)
