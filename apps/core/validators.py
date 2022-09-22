from django.utils.deconstruct import deconstructible
from rest_framework.validators import ValidationError
import phonenumbers


@deconstructible
class PhoneValidator:
    requires_context = False

    @staticmethod
    def is_integer(value):
        try:
            if int(value):
                return True
        except ValueError:
            return False

    @staticmethod
    def validate(value):
        try:
            item = phonenumbers.parse("+998" + value)
            if phonenumbers.is_valid_number(item):
                return True
        except Exception as e:
            return False
        return False

    def __call__(self, value):
        if not PhoneValidator.validate(value) or not PhoneValidator.is_integer(value):
            raise ValidationError("Nato'g'ri telefon raqam")
