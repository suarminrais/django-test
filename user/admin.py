from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserTypeChoices

# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
        required = (
            "email",
            "first_name",
            "last_name",
        )
    
    def _post_clean(self):
        super()._post_clean()
        user_type = self.cleaned_data.get("user_type")
        if user_type == UserTypeChoices.EMPLOYEE:
            self.fields["company"].required = True
            error = ValidationError(
                "This field is required.",
                code="company_not_be_null",
            )
            self.add_error("company", error)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2",
                "first_name", "last_name", "user_type", "company",
            )}
        ),
    )


admin.site.register(User, CustomUserAdmin)
