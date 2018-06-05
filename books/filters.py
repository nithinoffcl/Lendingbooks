#from django.contrib.auth.models import User
import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ["username","collegename","email","phonenumber","address","password","retypepassword"]
