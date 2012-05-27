"""
=====
Forms
=====

Some standard form types for use with our crispy extensions
"""

__author__ = 'Andy Theyers <@offmessage>'
__docformat__ = 'restructuredtext en'


from django.forms.models import ModelForm


class ModelFormWithFormsets(ModelForm):
    """
    Here we add functionality that assumes that we have a crispy form that
    uses our extensions
    """
    def is_valid(self):
        formsetcontainers = self.helper.formsets
        valid = []
        for formsetcontainer in formsetcontainers:
            formset = formsetcontainer.get_bound(self)
            valid.append(formset.is_valid())
        valid.append(super(ModelFormWithFormsets, self).is_valid())
        return all(valid)
    
    
