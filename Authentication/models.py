from django.db import models
from django.contrib.auth.models import User #AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from django.db import  IntegrityError
from .services import unique_otp_generator
from django.utils.crypto import get_random_string

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a unique verification token before saving
        if not self.token:
            self.token = get_random_string(length=64)
            while EmailVerificationToken.objects.filter(token=self.token).exists():
                self.token = get_random_string(length=64)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'token generated for {self.user}'

class PhoneBook(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    otp = models.CharField(max_length=10, unique=True)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.phone,self.otp)


def pre_save_create_OTP(sender, instance, *args, **kwargs):
    if not instance.otp:
        instance.otp= unique_otp_generator(instance)
pre_save.connect(pre_save_create_OTP,sender=PhoneBook)	











# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)

#         user.set_password(password)
#         user.save()

#         return user

#     def create_superuser(self, name, email, password=None, **extra_fields):
#         user = self.create_user(name, email, password=password, **extra_fields)
#         user.is_active = True
#         user.is_staff = True
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False) 
#     is_admin = models.BooleanField(default=False)

#     objects = UserAccountManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name

#     def __str__(self):
#         return self.email