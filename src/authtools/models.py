from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from captcha.fields import CaptchaField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255, unique=True,
                              db_index=True,)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

@python_2_unicode_compatible
class AbstractNamedUser(AbstractEmailUser):
    name = models.CharField(_('name'), max_length=255)
    phone_no = models.PositiveIntegerField(_('phone No'), default=0)
    gender = models.CharField(_('gender'), max_length=6)
    dob = models.DateField(_('date of birth'), default=datetime.date(datetime.now()))
    aadhar = models.CharField(_('aadhar'), max_length=12)
    

    REQUIRED_FIELDS = ['name','phone_no','gender','dob']

    class Meta:
        abstract = True
        ordering = ['name', 'email','phone_no', 'gender', 'dob', 'aadhar']

    def __str__(self):
        return '{name} {email} {phone_no}'.format(
            name=self.name,
            email=self.email,
            phone_no=self.phone_no,
        )

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]


class User(AbstractNamedUser):
    class Meta(AbstractNamedUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    objects = UserManager()
