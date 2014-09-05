from django import forms
from django.core.exceptions import MultipleObjectsReturned
from .models import User, Contact


class SignUpForm(forms.ModelForm):

    """
    Form that used to represent sign up form. There are three inputs username, email, and password.
    """

    error_messages = {
        'duplicate_username': ("Username sudah digunakan."),
        'duplicate_email': ("Email sudah digunakan."),
    }

    username = forms.RegexField(label=("Username"), max_length=30, regex=r'^[\w.@+-]+$',
                                help_text=("Harus ada. Maksimal 30 karakter. Hanya huruf, angka, dan @/./+/-/_."),
                                error_messages={'invalid': ("Hanya boleh mengandung huruf, angka, dan "
                                                            "@/./+/-/_.")})
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_email(self):
        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM.
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        except MultipleObjectsReturned:
            pass
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserCreationAdminForm(forms.ModelForm):

    """
    A form that creates a user, with no privileges, from the given username and password. Use it as the alternative
    of UserCreationForm for admin page. UserCreationForm bind into the old User model. This one is used for custom
    User model
    """

    error_messages = {
        'duplicate_username': ("A user with that username already exists."),
        'password_mismatch': ("The two password fields didn't match."),
    }
    username = forms.RegexField(label=("Username"), max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text=("Required. 30 characters or fewer. Letters, digits and "
                                           "@/./+/-/_ only."),
                                error_messages={
                                    'invalid': ("This value may contain only letters, numbers and "
                                                "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SignInForm(forms.Form):
    username_or_email = forms.RegexField(label=("Username"), max_length=100, regex=r'^[\w.@+-]+$',
                                         help_text=(
                                             "Harus ada. Maksimal 30 karakter. Hanya huruf, angka, dan @/./+/-/_."),
                                         error_messages={'invalid': ("Hanya boleh mengandung huruf, angka, dan "
                                                                     "@/./+/-/_.")})
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("name", "email", "address", "telephone", "message")


class ForgotPasswordForm(forms.Form):

    email = forms.CharField(max_length=200, required=True)

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(
                'Email not exist',
                code='email_not_exist',
            )
        return email
