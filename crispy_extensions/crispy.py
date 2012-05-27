"""
=================
Crispy extensions
=================

Trying to implement inline formsets within Crispy Forms.  Based on this pull
request to uni_form (that Miguel refused), plus my own Generic
https://github.com/pydanny/django-uni-form/pull/69/files
"""

__author__ = 'Andy Theyers <@offmessage>'
__docformat__ = 'restructuredtext en'


from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.forms.formsets import DELETION_FIELD_NAME
from django.forms.models import ModelForm
from django.template import Context
from django.template.loader import render_to_string

from crispy_forms.helpers import render_field

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'bootstrap')


class FormsetContainer(object):
    """
    Store formsets
    """
    def __init__(self, name, klass, prefix=None):
        self.name = name
        self.klass = klass
        self.prefix = prefix
        
    def get_bound(self, form):
        return getattr(form, self.name, None)
    
    def construct(self, kwargs):
        """Construct the formset"""
        return self.klass(**kwargs)
    
    def save(self, boundformset, instance=None):
        """How does your formset want to save?"""
        pass
        
        
    