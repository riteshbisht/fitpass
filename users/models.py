from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from .choices import (
    GENDER_CHOICES,
    MARITAL_STATUS_CHOCIES,
    ROLE_CHOCIES
)
from django.utils import timezone


class AbstractAutoDate(models.Model):
    created = models.DateTimeField(editable=False, auto_now_add=True,)
    modified = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, AbstractAutoDate):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'



class UserProfile(AbstractAutoDate):
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES)
    marital_status = models.PositiveSmallIntegerField(choices=MARITAL_STATUS_CHOCIES)
    user = models.OneToOneField(User, related_name='user_profile')


class Role(AbstractAutoDate):
    role_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.role_name


class UserRoles(AbstractAutoDate):
    user = models.ForeignKey(User, related_name='roles', verbose_name=_('User'))
    role = models.ForeignKey(Role, related_name='users', verbose_name=_('Role'))
    active = models.BooleanField(default=True)
