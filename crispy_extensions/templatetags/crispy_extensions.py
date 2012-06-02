"""
=================
My crispy filters
=================

Some additional filters that help with our more unusual layouts
"""

__author__ = 'Andy Theyers <@offmessage>'
__docformat__ = 'restructuredtext en'


from django.conf import settings
from django.forms.formsets import BaseFormSet
from django.template import Context
from django.template.loader import get_template
from django import template

from crispy_forms.helper import FormHelper


register = template.Library()

def flattener(form):
    """
    receive a crispy form and work our way down it to get a matching field list
    in the right order
    """
    res = []
    def _flattener(layout):
        for field in layout.fields:
            if isinstance(field, basestring):
                if field in form.fields:
                    res.append(field)
            else:
                _flattener(field)
        return res
    return _flattener(form.helper.layout)
                
@register.filter
def crispy_table_header(formset):
    """ 
    """
    template = get_template('crispy_extensions/tabular-form-header.html')
    
    form = formset.empty_form
    visible_fields = [ form[f] for f in flattener(form) if not form[f].is_hidden ]
    columncount = len(visible_fields)
    if formset.can_delete:
        columncount += 1
    if formset.can_order:
        columncount += 1
    data = {'formset': formset,
            'visible_fields': visible_fields,
            'column_count': columncount,
            'can_delete': formset.can_delete,
            'can_order': formset.can_order,
            }
    c = Context(data)
    return template.render(c)

@register.filter
def crispy_column_count(formset):
    form = formset.empty_form
    print form.fields
    print form.helper.layout.fields
    visible_fields = [ form[f] for f in flattener(form) if not form[f].is_hidden ]
    columncount = len(visible_fields)
    if formset.can_delete:
        columncount += 1
    if formset.can_order:
        columncount += 1
    return columncount
