# coding:utf-8
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, gender, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True,
                          gender=gender, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None,
                    gender=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password,
                                 gender, **extra_fields)

    def create_superuser(self, username, email, password,
                         gender, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password,
                                 gender, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user
    """

    username = models.CharField(
        _('username'), max_length=30, unique=True,
        help_text=_(
            'Required. 30 characters or fewer. Letters, digits and '
            '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only '
                                        'letters, numbers '
                                        'and @/./+/-/_ characters.'),
                                      'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    email = models.EmailField(_('email address'), blank=True)

    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField('Gender', choices=GENDER,
                              default=GENDER[0][0], max_length=1)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'gender']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser


