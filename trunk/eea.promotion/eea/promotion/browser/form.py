from zope.formlib.form import Fields
from zope.component import adapts
from zope.app.form.browser import MultiSelectWidget, SelectWidget
from zope.app.form.browser.itemswidgets import MultiCheckBoxWidget 
from Products.Five.formlib.formbase import EditForm as BaseEditForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser.widget import SimpleInputWidget
from eea.promotion.interfaces import IPromotion
from eea.promotion.vocabulary import FrontPageSectionsVocabulary


class CheckboxWidget(MultiCheckBoxWidget):

    def __init__(self, field, request):
        MultiCheckBoxWidget.__init__(self, field, field.value_type.vocabulary, request)

    def __call__(self):
        checkboxes = super(CheckboxWidget, self).__call__()
        return '<span id="%s">%s</span>' % (self.name, checkboxes)


class ThemesWidget(MultiSelectWidget):

    def __init__(self, field, request):
        MultiSelectWidget.__init__(self, field, field.value_type.vocabulary, request)


class LocationsWidget(SimpleInputWidget):

    def __call__(self):
        return '<input name="%s" type="hidden" value="%s" />' % (self.name, self._getFormValue())

    def _toFieldValue(self, input):
        if input == None:
            return []
        return input.replace("'", "").split(', ')
    
    def _toFormValue(self, value):
        return u', '.join(value)


class EditForm(BaseEditForm):
    """Form to edit promotions"""

    form_fields = Fields(IPromotion)
    form_fields = form_fields.omit('active')
    form_fields['locations'].custom_widget = LocationsWidget
    form_fields['themes'].custom_widget = ThemesWidget
    label = u'Edit Promotion'
    template = ViewPageTemplateFile('form.pt')
