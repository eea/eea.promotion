from zope.formlib.form import Fields
from Products.Five.formlib.formbase import EditForm as BaseEditForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser.widget import SimpleInputWidget
from eea.promotion.interfaces import IPromotion


class LocationsWidget(SimpleInputWidget):

    def __call__(self):
        return '<input name="%s" type="hidden" value="%s" />' % (self.name, self._getFormValue())

    def _toFieldValue(self, input):
        if input == None or input == u'':
            return []
        return input.replace("'", "").split(', ')
    
    def _toFormValue(self, value):
        return u', '.join(value)


class EditForm(BaseEditForm):
    """Form to edit promotions"""

    form_fields = Fields(IPromotion)
    form_fields = form_fields.omit('active')
    form_fields = form_fields.omit('themes')
    form_fields = form_fields.omit('themepage_section')
    form_fields['locations'].custom_widget = LocationsWidget
    label = u'Edit Promotion'
    template = ViewPageTemplateFile('form.pt')


def promotion_modified(obj, event):
    # TODO only reindex from our promotion edit form...
    obj.reindexObject()
