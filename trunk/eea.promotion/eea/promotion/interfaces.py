from zope.interface import Interface, Attribute
from zope.schema import Choice, Bool, Set


class IPromotion(Interface):
     
    """A promoted item can have a number of promotions"""
    
    locations = Set(
            title = u"Website locations",
            description = u"Where on the site to display this promotion.",
            required = True,
            value_type = Choice(vocabulary=u"Allowed Promotion Locations")
        )

    frontpage_section = Choice(
            title = u"Front Page Section",
            description = u"Which page section to put this promotion in.",
            required = True,
            vocabulary = u"Allowed Front Page Promotion Sections"
        )

    themepage_section = Choice(
            title = u"Theme Page Section",
            description = u"Which page section to put this promotion in.",
            required = True,
            vocabulary = u"Allowed Theme Page Promotion Sections"
        )

    themes = Set(
            title = u"Themes(s)",
            description = u"Which Themes(s) to apply.",
            required = True,
            value_type=Choice(vocabulary=u"Allowed Promotion Themes")
        )

    active = Bool(
            title = u"Activated",
            description = u"Activate/Deactivate this promotion.",
            required = True,
        )


class IPromoted(Interface):

    """Marker interface for promoted items"""


class IPromotable(Interface):

    """Marker interface for promotable content types"""
