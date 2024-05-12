from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _lazy

from mysite.apps.core.models import BaseModel


class User(AbstractUser, BaseModel):
    """
    Default custom user model for mysite.
    """

    class Meta:
        verbose_name = _lazy("User")

    def __str__(self) -> str:
        return f"{self.username}"
