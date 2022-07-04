from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County, State or Locality",
            "default_postcode": "Postal Code",
        }
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs[
                    "placeholder"
                ] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "fs-6 mb-3 small profile-form-input"
            self.fields[field].label = False
            self.fields[field].help_text = None


class UpdateUserForm(forms.ModelForm):
    """
    Update the user form to include the username,
    first name, last name, and email fields.
    """

    username = forms.CharField(
        max_length=100,
        required=True,  # username is required
        widget=forms.TextInput(attrs={"class": "form-control autofocus"}),
    )
    first_name = forms.CharField(
        required=True,  # first name is required
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        required=True,  # last name is required
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        required=True,  # email is required
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
