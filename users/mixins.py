from django.core.exceptions import PermissionDenied
from django.forms import ModelForm, BooleanField


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ManagerMixin:
    """Проверяет менеджера"""

    def get_queryset(self):
        queryset = super().get_queryset()
        perms = ['users.view_user', 'users.change_user']
        if self.request.user.has_perms(perms):
            return queryset
        raise PermissionDenied
