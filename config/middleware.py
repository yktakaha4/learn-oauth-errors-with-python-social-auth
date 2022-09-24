from social_core.exceptions import AuthCanceled
from social_django.middleware import SocialAuthExceptionMiddleware


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        if isinstance(exception, AuthCanceled):
            # TODO: 本当はここで適切なエラーメッセージを表示したい
            pass

        return f"ログインに失敗しました（例外: {exception.__class__.__name__}）"
