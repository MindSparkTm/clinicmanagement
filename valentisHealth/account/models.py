from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse


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
        regex=r'^[0-9]{9,15}$', message="Enter a valid phone number (9 - 15 digits).")
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