from urllib.parse import quote

from django.conf import settings
from social_core.exceptions import AuthCanceled
from social_django.middleware import SocialAuthExceptionMiddleware


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_redirect_uri(self, request, exception):
        # https://python-social-auth.readthedocs.io/en/latest/configuration/django.html?highlight=error#exceptions-middleware

        if isinstance(exception, AuthCanceled):
            error_message = None
        else:
            error_message = f"{type(exception).__name__}: {exception}"

        if error_message:
            return f"{settings.REDIRECT_URL}?error_message={quote(error_message)}"
        else:
            return settings.REDIRECT_URL
