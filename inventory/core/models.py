""" The models module, to define the objects blueprints """
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Super user model """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """
    email = models.EmailField(blank=True, default='', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#    def get_full_name(self):
#        return self.name

#    def get_short_name(self):
#        return self.name or self.email.split('0')[0]

    def __str__(self):
        return self.email

class Product(models.Model):
    """
    The model for all products
    """
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_stock_level = models.IntegerField()

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, description: \
        {self.description}"

class Stock(models.Model):
    """
    The model for stocks
    """

    TYPE_CHOICES= (
            ("in", "in"),
            ("out", "out"),
            )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    def __str__(self):
        return f"name: {self.product.name}, type: {self.type}, quantity: {self.quantity}"

class Supplier(models.Model):
    """
    The suppliers model
    """
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    products_supplied = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"name: {self.name} contact_info: {self.contact_info}"
