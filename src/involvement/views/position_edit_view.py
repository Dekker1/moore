from wagtail.contrib.modeladmin.views import EditView
from involvement.models import Role
from involvement.rules import is_admin


class PositionEditView(EditView):
    def get_form(self, form_class=None):
        form = super(PositionEditView, self).get_form(form_class=form_class)
        queryset = form.fields['role'].queryset
        if not is_admin(self.request.user):
            queryset = Role.edit_permission_of(self.request.user)

        init = Role.objects.get(pk=form.initial['role'])
        if not init.archived:
            queryset = queryset.filter(
                archived=False
            )

        form.fields['role'].queryset = queryset
        return form
