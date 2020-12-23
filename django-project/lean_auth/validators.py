import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w.-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = _(
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    flags = 0
