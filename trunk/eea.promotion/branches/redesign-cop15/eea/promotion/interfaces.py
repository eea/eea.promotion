from zope.interface import Interface, Attribute
from zope.schema import Choice, Bool, Set, List


class IPromotion(Interface):
     
    """A promoted item can have a number of promotions"""
    
    locations = List(
            title = u"Website locations",
            description = u"Where on the site to display this promotion.",
            required = False,
        )

    themepage_section = Choice(
            title = u"Theme Page Section",
            description = u"Which page section to put this promotion in.",
            required = False,
            vocabulary = u"Themepage Promotion Sections"
        )

    themes = List(
        title = u"Themes",
        description = u"List of themes that this content object should be "
                       "associated with. If this promotion should be visible "
                       "on theme pages, this list is used to determine on "
                       "which themes.",
        required = False,
        max_length = 3,
        value_type = Choice(
            title = u"Theme",
            vocabulary = u"Allowed themes",
            )
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

    display_globally = Bool(
            title = u"Display On All Pages",
            description = u"Whether or not this promotion should be visible \
                    on all pages",
        )

    remove = Attribute("Remove all annotations stored in this promotion")

    edit_url = Attribute("URL to edit this promotion")

    is_external  = Attribute("Is this an external or internal promotion?")

    url = Attribute("Get the URL to this promotion")


class IPromoted(Interface):

    """Marker interface for promoted items"""


class IPromotable(Interface):

    """Marker interface for promotable content types"""


class IFrontpageSectionIndex(Interface):

    """Returns which frontpage section the promotion is in"""

class IGlobalPromotion(Interface):
    
    """Returns the first global promotion found"""
