from zope.formlib.form import Fields
from zope.component import adapts
from zope.app.form.browser import MultiSelectWidget
from Products.Five.formlib.formbase import EditForm as BaseEditForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser.widget import SimpleInputWidget
from eea.promotion.interfaces import IPromotion
from eea.promotion.vocabulary import FrontPageSectionsVocabulary
from zope.app.form.browser.itemswidgets import MultiCheckBoxWidget 


class CheckboxWidget(MultiCheckBoxWidget):

    def __init__(self, field, request):
        MultiCheckBoxWidget.__init__(self, field, field.value_type.vocabulary, request)

    def __call__(self):
        checkboxes = super(CheckboxWidget, self).__call__()
        return '<span id="%s">%s</span>' % (self.name, checkboxes)


class EditForm(BaseEditForm):
    """Form to edit promotions"""

    form_fields = Fields(IPromotion)
    form_fields = form_fields.omit('active')
    form_fields['locations'].custom_widget = CheckboxWidget
    form_fields['themes'].custom_widget = CheckboxWidget
    label = u'Edit Promotion'
    template = ViewPageTemplateFile('edit.pt')
