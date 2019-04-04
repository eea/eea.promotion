""" Interfaces
"""
from zope.interface import Interface, Attribute
from zope.schema import Choice, Bool, List


class IPromotion(Interface):
    """ A promoted item can have a number of promotions
    """
    locations = List(
            title=u"Website locations",
            description=u"Where on the site to display this promotion.",
            required=False,
        )

    themepage_section = Choice(
            title=u"Theme Page Section",
            description=u"Which page section to put this promotion in.",
            required=False,
            vocabulary=u"Themepage Promotion Sections"
        )

    themes = List(
        title=u"Themes",
        description=u"List of themes that this content object should be "
                       "associated with. If this promotion should be visible "
                       "on theme pages, this list is used to determine on "
                       "which themes.",
        required=False,
        max_length=3,
        value_type=Choice(
            title=u"Theme",
            vocabulary=u"Allowed themes",
            )
        )

    active = Bool(
            title=u"Activated",
            description=u"Activate/Deactivate this promotion.",
        )

    display_on_frontpage = Bool(
            title=u"Display On Front Page",
            description=u"Whether or not this promotion should be visible \
                    on the front page.",
        )

    display_on_themepage = Bool(
            title=u"Display On Themes Page",
            description=u"Whether or not this promotion should be visible \
                    on the themes page.",
        )

    display_in_spotlight = Bool(
            title=u"Display In Spotlight",
            description=u"Whether or not this promotion should be visible \
                    in spotlight",
        )

    display_in_topics_index_page = Bool(
        title=u"Display In Topics index page",
        description=u"Whether or not this promotion should be visible \
                    in topics index page",
    )

    display_on_datacentre = Bool(
            title=u"Display In Datacentre",
            description=u"Whether or not this promotion should be visible \
                    on datacentres",
        )

    edit_url = Attribute("URL to edit this promotion")

    is_external = Attribute("Is this an external or internal promotion?")

    url = Attribute("Get the URL to this promotion")

    def remove(self):
        """ Remove all annotations stored in this promotion
        """

class IPromoted(Interface):
    """ Marker interface for promoted items
    """

class IPromotable(Interface):
    """ Marker interface for promotable content types
    """

class IFrontpageSectionIndex(Interface):
    """ Returns which frontpage section the promotion is in
    """
