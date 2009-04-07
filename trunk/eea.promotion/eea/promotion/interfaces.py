from zope.interface import Interface, Attribute
from zope.schema import Choice


class IPromotedItem(Interface):
     
    """A promoted item can have a number of promotions"""
    
    location = Choice(
            title = u"Location",
            description = u"Where you want this promotion to be displayed",
            required = True,
            vocabulary = "Promotion Locations",
        )

    visibility = Choice(
            title = u"Visibility",
            description = u"Where you want this promotion to be displayed",
            required = True,
            vocabulary = "Promotion Visibility Levels",
        )


class IPromotable(Interface):

    """Marker interface for promotable content types"""
