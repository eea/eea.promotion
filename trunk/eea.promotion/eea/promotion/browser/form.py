from zope.formlib.form import Fields
from zope.component import adapts
from Products.Five.formlib.formbase import EditForm as BaseEditForm
from eea.promotion.interfaces import IPromotion


class EditForm(BaseEditForm):

    """ """

    form_fields = Fields(IPromotion)
    label = u'Edit Promotion'
