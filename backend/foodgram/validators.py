import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AllowedCharactersUsernameValidator:
    def __init__(self, pattern=r'^[\w.@+-]+$'):
        self.pattern = pattern
        self.regex = re.compile(pattern)

    def __call__(self, value):
        if not self.regex.fullmatch(value):
            raise ValidationError(
                'Имя пользователя может содержать только буквы стандартной '
                'латиницы, цифры 0-9 и символы "@", ".", "+", "-", "_".'
            )

    def get_help_text(self):
        return (
            'Имя пользователя может содержать только буквы стандартной '
            'латиницы, цифры 0-9 и символы "@", ".", "+", "-", "_".'
        )
