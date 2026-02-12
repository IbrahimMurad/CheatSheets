# Django Allauth

## Installation

```bash
pip install django-allauth
```

Or,

```bash
pip install "django-allauth[socialaccount]"
```

For social authentication.

Or,

```bash
pip install "django-allauth[mfa]"
```

For multifactor authentication.

## Important configurations in `settings.py` file

```python
# Specify the context processors as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]

INSTALLED_APPS = [
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.messages',

    'allauth',
    'allauth.account',

    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.amazon_cognito',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.digitalocean',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.edx',
    'allauth.socialaccount.providers.facebook',,
    'allauth.socialaccount.providers.figma',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.jupyterhub',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.notion',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.openid_connect',
    'allauth.socialaccount.providers.patreon',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.pinterest',
    'allauth.socialaccount.providers.reddit',
    'allauth.socialaccount.providers.shopify',
    'allauth.socialaccount.providers.slack',
    'allauth.socialaccount.providers.snapchat',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.spotify',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.steam',
    'allauth.socialaccount.providers.telegram',
    'allauth.socialaccount.providers.trello',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.tumblr_oauth2',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.twitter_oauth2',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vimeo_oauth2',
    'allauth.socialaccount.providers.windowslive',
    'allauth.socialaccount.providers.yahoo',
    'allauth.socialaccount.providers.zoom',
    ...
]

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
)

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}
```

## Usefull urls

```python3
// urls.py

urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

## Post Installation

```
python manage.py migrate
```

## Regular Account

### Configurations

```python

# -------------------------------------------------------------------------------------------------------------------------------
# Overall
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
ACCOUNT_PREVENT_ENUMERATION = True  # Controls whether or not information is revealed about whether or not a user account exists
ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m/user",
    "change_phone": "1/m/user",
    "manage_email": "10/m/user",
    "reset_password": "20/m/ip,5/m/key",
    "reauthenticate": "10/m/user",
    "reset_password_from_key": "20/m/ip",
    "signup": "20/m/ip",
    "login": "30/m/ip",
    "login_failed": "10/m/ip,5/5m/key",
    "confirm_email": "1/3m/key" # this for link or "1/10s/key" for code
}  # or False for no rate limiting

ACCOUNT_SESSION_REMEMBER = None # to ask the user (“Remember me?”), `False` to not remember, and `True` to always remember.

ACCOUNT_TEMPLATE_EXTENSION = "html"

ACCOUNT_FORMS = {
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'confirm_login_code': 'allauth.account.forms.ConfirmLoginCodeForm',
    'login': 'allauth.account.forms.LoginForm',
    'request_login_code': 'allauth.account.forms.RequestLoginCodeForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'signup': 'allauth.account.forms.SignupForm',
    'user_token': 'allauth.account.forms.UserTokenForm',
}

# -------------------------------------------------------------------------------------------------------------------------------
# Signup
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_SIGNUP_FIELDS = ['username*', 'email', 'password1*', 'password2*']
ACCOUNT_SIGNUP_FORM_CLASS = None
"""A string pointing to a custom form class (e.g. 'myapp.forms.SignupForm') that is used during signup to ask the user for additional input (e.g. a newsletter signup checkbox, or birth date). This class should derive from just forms.Form and only list the additional fields you need. It must implement a def signup(self, request, user) method, which is called during the signup process. This method allows you to handle and store the submitted data as needed."""

ACCOUNT_SIGNUP_FORM_HONEYPOT_FIELD = None
"""
A string value that will be used as the HTML ‘name’ property on a honeypot input field on the sign up form. Honeypot fields are hidden to normal users but might be filled out by naive spam bots. When the field is filled out the app will not create a new user and attempt to fool the bot with a fake successful response. We recommend setting this to some believable value that your app does not actually collect on signup e.g. ‘phone_number’ or ‘address’. Honeypots are not always successful for sophisticated bots so this should be used as one layer in a suite of spam detection tools if your site is having trouble with spam.
"""

# -------------------------------------------------------------------------------------------------------------------------------
# Login
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_LOGIN_BY_CODE_ENABLED = False
"""
“Login by email” offers an alternative method of logging in. Instead of entering an email address and accompanying password, the user only enters the email address. Then, a one-time code is sent to that email address which allows the user to login. This method is often referred to as “Magic Code Login”. This setting controls whether or not this method of logging in is enabled.
"""

ACCOUNT_LOGIN_BY_CODE_TRUST_ENABLED = False
"""
Indicates whether the MFA “Trust this browser?” functionality is to be enabled for logging in by code. Note that this requires the MFA app to be installed.
"""
ACCOUNT_LOGIN_BY_CODE_MAX_ATTEMPTS = 3

ACCOUNT_LOGIN_BY_CODE_REQUIRED = False
"""
When enabled (in case of True), every user logging in is required to input a login confirmation code sent by email. Alternatively, you can specify a set of authentication methods ("password", "mfa", or "socialaccount") for which login codes are required.
"""

ACCOUNT_LOGIN_BY_CODE_TIMEOUT = 180

ACCOUNT_LOGIN_METHODS = {"username"} # options: "email" or "username"

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_LOGIN_TIMEOUT = 900

# -------------------------------------------------------------------------------------------------------------------------------
# Logout
# -------------------------------------------------------------------------------------------------------------------------------
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

# -------------------------------------------------------------------------------------------------------------------------------
# Password Reset
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
"""
`render_value` parameter as passed to PasswordInput fields.
"""

ACCOUNT_PASSWORD_RESET_BY_CODE_ENABLED = False

ACCOUNT_PASSWORD_RESET_BY_CODE_MAX_ATTEMPTS = 3

ACCOUNT_PASSWORD_RESET_BY_CODE_TIMEOUT = 180

ACCOUNT_PASSWORD_RESET_TOKEN_GENERATOR = "allauth.account.forms.EmailAwarePasswordResetTokenGenerator"

# -------------------------------------------------------------------------------------------------------------------------------
# Email Verification
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
"""
In order to verify an email address, a key is mailed identifying the email address to be verified. In previous versions, a record was stored in the database for each ongoing email confirmation, keeping track of these keys. Current versions use HMAC based keys that do not require server side state.
"""

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_EMAIL_VERIFICATION = "optional" # options: "mandatory", "optional", or "none"

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_MAX_ATTEMPTS = 3

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_TIMEOUT = 900

ACCOUNT_EMAIL_VERIFICATION_SUPPORTS_CHANGE = False
"""
Whether or not the email can be changed after signup at the email verification stage.
"""

ACCOUNT_EMAIL_VERIFICATION_SUPPORTS_RESEND = False

# -------------------------------------------------------------------------------------------------------------------------------
# Reauthentication
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_REAUTHENTICATION_TIMEOUT = 300

ACCOUNT_REAUTHENTICATION_REQUIRED = False

# -------------------------------------------------------------------------------------------------------------------------------
# Routing
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
"""
The default behaviour is to redirect authenticated users to LOGIN_REDIRECT_URL when they try accessing login/signup pages.
By changing this setting to False, logged in users will not be redirected when they access login/signup pages.
"""
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = settings.LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_LOGOUT_REDIRECT_URL = settings.LOGOUT_REDIRECT_URL # or "/"
ACCOUNT_SIGNUP_REDIRECT_URL = settings.LOGIN_REDIRECT_URL

# -------------------------------------------------------------------------------------------------------------------------------
# Sending Email
# -------------------------------------------------------------------------------------------------------------------------------
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Site]"
"""
Subject-line prefix to use for email messages sent. By default, the name of the current Site (django.contrib.sites) is used.
"""

ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = True
"""
When enabled, users who attempt to log in with an unknown email address are sent an email message containing a link that allows them to create an account and log in. This setting is disabled by default.
"""

ACCOUNT_EMAIL_NOTIFICATIONS = False
"""
When enabled, account related security notifications, such as “Your password was changed”, including information on user agent / IP address from where the change originated, will be emailed.
"""

# -------------------------------------------------------------------------------------------------------------------------------
# Email Addresses
# -------------------------------------------------------------------------------------------------------------------------------

ACCOUNT_CHANGE_EMAIL = False
ACCOUNT_EMAIL_MAX_LENGTH = 254
ACCOUNT_MAX_EMAIL_ADDRESSES = None
ACCOUNT_UNIQUE_EMAIL = True

# -------------------------------------------------------------------------------------------------------------------------------
# User Model
# -------------------------------------------------------------------------------------------------------------------------------
ACCOUNT_PRESERVE_USERNAME_CASING = True
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USER_DISPLAY = "some.module.callable_name"  # A callable returning the displayed username
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_MIN_LENGTH = 1
ACCOUNT_USERNAME_VALIDATORS = None  # 'some.module.validators.custom_username_validators'
```

### Views

| The view                         | path                                                    | url name                                 | endpoint url                                |
| -------------------------------- | ------------------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| Login                            | `allauth.account.views.LoginView`                       |`account_login`                           | `/accounts/login/`                          |
| Signup                           | `allauth.account.views.SignupView`                      | `account_signup`                         | `/accounts/signup/`                         |
| Logout                           | `allauth.account.views.LogoutView`                      | `account_logout`                         | `/accounts/logout/`                         |
| Password Set                     | `allauth.account.views.PasswordSetView`                 | `account_set_password`                   | `/accounts/password/set/`                   |
| Password Change                  | `allauth.account.views.PasswordChangeView`              | `account_change_password`                | `/accounts/password/change/`                |
| Password Reset                   | `allauth.account.views.PasswordResetView`               | `account_reset_password`                 | `/accounts/password/reset/`                 |
| Password Reset From Key          | `allauth.account.views.PasswordResetFromKeyView`        | `account_reset_password_from_key`        | `/accounts/password/reset/key/`             |
| Password Reset Done              | `allauth.account.views.PasswordResetDoneView`           | `account_reset_password_done`            | `/accounts/password/reset/done/`            |
| Password Reset Confirm           | `allauth.account.views.PasswordResetConfirmView`        | `account_reset_password_confirm`         | `/accounts/password/reset/confirm/`         |
| Password Reset Confirm Done      | `allauth.account.views.PasswordResetConfirmDoneView`    | `account_reset_password_confirm_done`    | `/accounts/password/reset/confirm/done/`    |
| Email                            | `allauth.account.views.EmailView`                       | `account_email`                          | `/accounts/email/`                          |
| Email Confirmation               | `allauth.account.views.ConfirmEmailView`                | `account_confirm_email`                  | `/accounts/confirm-email/`                  |
| Email Confirmation Done          | `allauth.account.views.ConfirmEmailDoneView`            | `account_confirm_email_done`             | `/accounts/confirm-email/done/`             |
| Email Confirmation From Key      | `allauth.account.views.ConfirmEmailFromKeyView`         | `account_confirm_email_from_key`         | `/accounts/confirm-email/key/`              |
| Email Confirmation From Key Done | `allauth.account.views.ConfirmEmailFromKeyDoneView`     | `account_confirm_email_from_key_done`    | `/accounts/confirm-email/key/done/`         |
| Email Confirmation Resend        | `allauth.account.views.EmailConfirmationResendView`     | `account_email_confirmation_resend`      | `/accounts/email/confirmation/resend/`      |
| Email Confirmation Resend Done   | `allauth.account.views.EmailConfirmationResendDoneView` | `account_email_confirmation_resend_done` | `/accounts/email/confirmation/resend/done/` |


### Template Tags

```html
{% load account %}

{% user_display user %}

Or,

{% load account %}

{% user_display user as user_display %}
{% blocktrans %}{{ user_display }} has logged in...{% endblocktrans %}

```


### Forms


| Action | path                               | used on                   |
| ------ | ---------------------------------- | ------------------------- |
| Login  | `allauth.account.forms.LoginForm`  | `account_login` view      |
| Signup | `allauth.account.forms.SignupForm` | `account_signup` view     |


Add Email
Path:
allauth.account.forms.AddEmailForm

Used on:
account_email view.

Example override:

from allauth.account.forms import AddEmailForm
class MyCustomAddEmailForm(AddEmailForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns an allauth.account.models.EmailAddress object.
        email_address_obj = super().save(request)

        # Add your own processing here.

        # You must return the original result.
        return email_address_obj
You have access to the following:

self.user is the User object that is logged in.

settings.py:

ACCOUNT_FORMS = {'add_email': 'mysite.forms.MyCustomAddEmailForm'}
Change Password
Path:
allauth.account.forms.ChangePasswordForm

Used on:
account_change_password view.

Example override:

from allauth.account.forms import ChangePasswordForm
class MyCustomChangePasswordForm(ChangePasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super().save()

        # Add your own processing here.
You have access to the following:

self.user is the User object that is logged in.

settings.py:

ACCOUNT_FORMS = {'change_password': 'mysite.forms.MyCustomChangePasswordForm'}
Set Password
Path:
allauth.account.forms.SetPasswordForm

Used on:
account_set_password view.

Example override:

from allauth.account.forms import SetPasswordForm
class MyCustomSetPasswordForm(SetPasswordForm):

    def save(self):

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super().save()

        # Add your own processing here.
You have access to the following:

self.user is the User object that is logged in.

settings.py:

ACCOUNT_FORMS = {'set_password': 'mysite.forms.MyCustomSetPasswordForm'}
Reset Password
Path:
allauth.account.forms.ResetPasswordForm

Used on:
account_reset_password view.

Example override:

from allauth.account.forms import ResetPasswordForm
class MyCustomResetPasswordForm(ResetPasswordForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super().save(request)

        # Add your own processing here.

        # Ensure you return the original result
        return email_address
You have access to the following:

self.users is a list of all possible User objects with matching email address.

settings.py:

ACCOUNT_FORMS = {'reset_password': 'mysite.forms.MyCustomResetPasswordForm'}
Reset Password From Key
Path:
allauth.account.forms.ResetPasswordKeyForm

Used on:
account_reset_password view.

Example override:

from allauth.account.forms import ResetPasswordKeyForm
class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):

    def save(self):

        # Add your own processing here.

        # Ensure you call the parent class's save.
        # .save() does not return anything
        super().save()
You have access to the following:

self.user is the User object.

settings.py:

ACCOUNT_FORMS = {'reset_password_from_key': 'mysite.forms.MyCustomResetPasswordKeyForm'}