from zope.formlib.form import Fields
from zope.component import adapts
from Products.Five.formlib.formbase import EditForm as BaseEditForm
from eea.promotion.interfaces import IPromotedItem


class EditForm(BaseEditForm):

    """ """

    form_fields = Fields(IPromotedItem)
    label = u'Create Promotion'
