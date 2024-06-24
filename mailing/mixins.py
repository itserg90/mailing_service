from django.core.exceptions import PermissionDenied


class UserAutofillMixin:
    """Присваивает объекту пользователя"""

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.request.user
        obj.user = user
        obj.save()
        return super().form_valid(form)


class OwnerMixin:
    """Проверяет собственника объекта"""

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.user:
            return self.object
        raise PermissionDenied


class OwnerManagerMixin:
    """Проверяет собственника объекта или менеджера"""

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        perms = ['mailing.can_disable_newsletter', 'users.can_disable_user']
        if self.request.user == self.object.user or self.request.user.has_perms(perms):
            return self.object
        raise PermissionDenied


class NotManagerMixin:
    """Проверяет, чтобы не был менеджером"""

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        perms = ['mailing.can_disable_newsletter', 'users.can_disable_user']
        if self.request.user.has_perms(perms):
            raise PermissionDenied
        return form


class KwargsMixin:
    """Добавляет пользователя в словарь для дальнейшей фильтраци данных по пользователю"""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
