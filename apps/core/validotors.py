from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneValidator:
    requires_context = False

    def __call__(self, value):
        try:
            int(value)
        except ValueError:
            raise ValidationError(
                _('%(value)s is not a number'),
                params={'value': value},
            )

