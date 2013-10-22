""" Form
"""
from zope.formlib.form import Fields
from five.formlib.formbase import EditForm as BaseEditForm
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.form.browser.widget import SimpleInputWidget
from eea.promotion.interfaces import IPromotion

class LocationsWidget(SimpleInputWidget):
    """ Location widget
    """

    def __call__(self):
        return '<input name="%s" type="hidden" value="%s" />' % \
               (self.name, self._getFormValue())

    def _toFieldValue(self, linput):
        """ To field
        """
        if linput == None or linput == u'':
            return []
        return linput.replace("'", "").split(', ')

    def _toFormValue(self, value):
        """ From
        """
        return u', '.join(value)

class EditForm(BaseEditForm):
    """ Form to edit promotions
    """
    form_fields = Fields(IPromotion)
    form_fields = form_fields.omit('active')
    form_fields = form_fields.omit('themes')
    form_fields = form_fields.omit('themepage_section')
    form_fields['locations'].custom_widget = LocationsWidget
    label = u'Edit Promotion'
    template = ViewPageTemplateFile('form.pt')

def promotion_modified(obj, event):
    """ Promotion modified
    """
    #TODO: only reindex from our promotion edit form ...
    obj.reindexObject()
