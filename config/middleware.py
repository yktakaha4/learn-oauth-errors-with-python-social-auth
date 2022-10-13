from requests import HTTPError
from social_core.exceptions import AuthCanceled, AuthMissingParameter
from social_django.middleware import SocialAuthExceptionMiddleware


class CustomizedSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        # サンプルアプリケーションのためエラーレベルが全て Error になっているが、
        # 実務においては process_exception を override してエラーレベルもハンドリングできるとよりベター
        # SPAの場合は、 get_redirect_uri を上書きしてエラーコードを含むURLに飛ばしてフロントでメッセージ表示もgood
        if isinstance(exception, AuthCanceled):
            # a. ユーザの操作に起因する認可エラー
            return "\u2139認証がキャンセルされました。ログインを希望する場合は、再度操作をおこなってください。"

        elif isinstance(exception, AuthMissingParameter):
            # b. ユーザーの環境に起因する認可エラー
            # エラー発生を監視システムに通知する（その上で無視する）
            self.capture_exception(exception)
            return "🚫認証に失敗しました。以下を確認し、再度操作をおこなってください。・Cookieが有効されていること・対応ブラウザでサイトを閲覧していること"

        elif isinstance(exception, HTTPError):
            # c. IdPに起因する認可エラー
            # エラー発生を監視システムに通知する（短時間で一定量発生しない限り無視する）
            self.capture_exception(exception)
            return (
                "🚫連携サービスの一時的な不具合により認証ができない状況になっています。しばらく待ってから再度操作するか、他のログイン方法をお試しください。"
            )

        else:
            # d. その他のエラー
            # エラー発生を監視システムに通知し、a. ~ c. のエラーに振り分けてよいか検討する
            self.capture_exception(exception)
            return "🚫認証に失敗しました。恐れ入りますが、しばらくしてから再度操作をおこなってください。"

    def capture_exception(self, exception):
        # Sentryなどのエラー監視システムにエラー情報を送信
        pass
