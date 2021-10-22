from django.contrib.auth.models import User
from django.db.models.base import Model


class CreateUserForm(Model):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
