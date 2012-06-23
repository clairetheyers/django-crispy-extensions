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
    def is_multipart(self):
        formsetcontainers = getattr(self.helper, 'formsets', [])
        is_multipart = [super(ModelFormWithFormsets, self).is_multipart(),]
        def test_multipart(formsetcontainer):
            # Test for multipart-ness, regardless of whether we've been fully
            # instantiated or not
            try:
                formset = getattr(self, formsetcontainer.name)
            except AttributeError:
                formset = formsetcontainer.klass
            form = None
            if hasattr(formset, 'forms'):
                try:
                    form = formset.forms[0]
                except IndexError:
                    pass
            else:
                form = formset.form
            if hasattr(form, 'fields'):
                fields = form.fields
            else:
                fields = form.base_fields
            return any([ f.widget.needs_multipart_form for f in fields.values() ])
        
        is_multipart.extend([ test_multipart(f) for f in formsetcontainers ])
        return any(is_multipart)
        
    def is_valid(self):
        formsetcontainers = getattr(self.helper, 'formsets', [])
        valid = []
        for formsetcontainer in formsetcontainers:
            formset = formsetcontainer.get_bound(self)
            valid.append(formset.is_valid())
        valid.append(super(ModelFormWithFormsets, self).is_valid())
        return all(valid)
    
    
