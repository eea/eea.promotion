from zope.interface import Interface, Attribute
from zope.schema import Choice


class IPromotion(Interface):
     
    """A promoted item can have a number of promotions"""
    
    section = Choice(
            title = u"Section",
            description = u"Where to display this promotion",
            required = True,
            vocabulary = "Promotion Sections",
        )

    visibility = Choice(
            title = u"Visibility",
            description = u"Degree of visibility",
            required = True,
            vocabulary = "Promotion Visibility Levels",
        )


class IPromoted(Interface):

    """Marker interface for promoted items"""


class IPromotable(Interface):

    """Marker interface for promotable content types"""
