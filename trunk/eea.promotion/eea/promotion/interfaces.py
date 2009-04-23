from zope.interface import Interface, Attribute
from zope.schema import Choice, Bool, Set, List


class IPromotion(Interface):
     
    """A promoted item can have a number of promotions"""
    
    locations = List(
            title = u"Website locations",
            description = u"Where on the site to display this promotion.",
            required = True,
        )

    frontpage_section = Choice(
            title = u"Front Page Section",
            description = u"Which page section to put this promotion in.",
            required = True,
            vocabulary = u"Frontpage Promotion Sections"
        )

    themepage_section = Choice(
            title = u"Theme Page Section",
            description = u"Which page section to put this promotion in.",
            required = True,
            vocabulary = u"Themepage Promotion Sections"
        )

    themes = Set(
            title = u"Themes(s)",
            description = u"Which Themes(s) to apply.",
            value_type=Choice(vocabulary=u"Allowed themes")
        )

    active = Bool(
            title = u"Activated",
            description = u"Activate/Deactivate this promotion.",
        )

    display_on_frontpage = Bool(
            title = u"Display On Front Page",
            description = u"Whether or not this promotion should be visible \
                    on the front page.",
        )

    display_on_themepage = Bool(
            title = u"Display On Themes Page",
            description = u"Whether or not this promotion should be visible \
                    on the themes page.",
        )


class IPromoted(Interface):

    """Marker interface for promoted items"""


class IPromotable(Interface):

    """Marker interface for promotable content types"""
