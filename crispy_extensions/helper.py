"""
=======
Helpers
=======

Additional attributes for the helpers
"""

__author__ = 'Andy Theyers <@offmessage>'
__docformat__ = 'restructuredtext en'


class FormsetContainer(object):
    """
    Store formsets. You're going to have to subclass this so it knows how to
    save its formsets.
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
        
    def is_multipart(self):
        """Does this form need a multipart form tag"""
        fields = self.klass.form.base_fields.values()
        return any([ f.widget.needs_multipart_form for f in fields ])
    
    def save(self, boundformset, instance=None):
        """How does your formset want to save?"""
        raise NotImplementedError("You need to define FormsetContainer.save() yourself")
        
        
