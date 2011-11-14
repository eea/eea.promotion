from zope.interface import Interface


class IAdminView(Interface):

    """ Custom view that gives an overview of all internal promotions on the site. """

    def find_promotions(): pass
