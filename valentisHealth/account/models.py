from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group, Permission
from django.urls import reverse
from django.utils.crypto import get_random_string, salted_hmac
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login, logout
import unicodedata

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(
        _('first name'), max_length=30, null=True)
    last_name = models.CharField(
        _('last name'), max_length=30, null=True)
    phone_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9]{9,15}$', message="Enter a valid phone number (9 - 15 digits).")
    phone_number = models.CharField(
        _('phone number'), max_length=30, null=True, validators=[phone_regex])
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    id_number = models.CharField(
        _('id number'), max_length=20, unique=True, null=True)
    staff_number = models.CharField(
        _('staff number'), max_length=30, unique=True, null=True)
    activation_key = models.CharField(max_length=40, blank=True, null=True)
    activation_key_expires = models.DateTimeField(blank=True, null=True)
    verification_code = models.IntegerField(blank=True, null=True)
    verification_code_expires = models.DateTimeField(blank=True, null=True)
    account_verified_date = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen'), blank=True, null=True)
    force_logout_date = models.DateTimeField(null=True)
    is_patient = models.BooleanField(default=False,
                                     help_text=_('Designates whether the user can log into the website.'))

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['id']
        default_permissions = ()
        permissions = (
            ('create_deactivate_user', 'Accounts - Can add/deactivate a user'),
            ('edit_user', 'Accounts - Can edit details of a user'),
        )

    def __unicode__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('system-user', kwargs={'pk': self.pk})

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def user_site(self):
        if self.is_site_user:
            try:
                site = self.site_user.get(is_active=True)
                return site.site
            except ObjectDoesNotExist:
                pass
        return None

    def random_password(self, length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):


        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        return get_random_string(length, allowed_chars)

    def send_confirmation(self, reciever_email):
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your ValentisHealth clinic account.'
        message = render_to_string('activate_email.html', {
            'user': self,
            'domain': current_site.domain,
            'email': self.email,
            'token': account_activation_token.make_token(self),
        })
        to_email = self.email

        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()

    def activate(self, request):
        self.is_active = True
        self.save()
        login(request, self)
        # return redirect('home')
        password = self.random_password()
        self.set_password(password)
        message = "Your password is: \n" + password + "\nYour username is: " + self.email
        self.email_user("Your Valentis Health Clinic System Password", message, from_email=None)
        print(password)
        # user.is_active = True
        self.save()
