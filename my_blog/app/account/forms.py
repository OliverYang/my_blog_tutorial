__author__ = 'oliver'

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from my_blog.app.account.models import CustomerUser


class CustomerUserCreateForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_css_class = 'has-error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomerUser
        fields = ('email',)


class CustomerUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    error_css_class = 'has-error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(CustomerUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomerUser
        fields = '__all__'


class UserAccountForm(ModelForm):
    error_css_class = 'has-error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(UserAccountForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomerUser
        fields = ['nickname', 'email']

        help_text = {
            'nickname': None,
            'email': None,
        }

    def clean_email(self):
        email = self.clean_date['email']
        if email.lower() == self.instance.email.lower():
            return email
        if CustomerUser.objects.filter(email__iexaxt=email).exists():
            raise forms.ValidationError(
                _('Email address already in use: %(value)s'),
                code='exists',
                params={'value': email})
        return email


class SuperuserAccountForm(ModelForm):

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = CustomerUser
        fields = ['email', 'nickname', 'is_active']

        help_text = {
            'email': None,
            'nickname': None,
        }